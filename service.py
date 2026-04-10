from __future__ import annotations

import json
import logging
import os
import shutil
import threading
import uuid
import zipfile
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from main import DEFAULT_USER_AGENT, build_manifest, crawl_docs

logger = logging.getLogger(__name__)

# On Vercel (and other read-only Lambda environments) only /tmp is writable.
_default_data_dir = "/tmp/doc_getter_runs" if os.getenv("VERCEL") else "runs"
DATA_ROOT = Path(os.getenv("DOC_GETTER_DATA_DIR", _default_data_dir)).resolve()
MAX_JOB_WORKERS = max(2, int(os.getenv("DOC_GETTER_JOB_WORKERS", "4")))
JOB_RETENTION_SECONDS = max(
    600,
    int(os.getenv("DOC_GETTER_JOB_RETENTION_SECONDS", str(12 * 60 * 60))),
)
DEFAULT_CORS_ORIGINS = ",".join(
    [
        "http://localhost:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:3001",
        "https://getdoc.tool.txzy.net",
    ]
)


def parse_cors_origins() -> list[str]:
    raw = os.getenv("DOC_GETTER_CORS_ORIGINS", DEFAULT_CORS_ORIGINS)
    origins = [item.strip() for item in raw.split(",") if item.strip()]
    return origins or ["*"]


CORS_ALLOW_ORIGINS = parse_cors_origins()
CORS_ALLOW_ORIGIN_REGEX = os.getenv(
    "DOC_GETTER_CORS_ORIGIN_REGEX",
    r"https?://(localhost|127\.0\.0\.1)(:\d+)?$|https://.*\.vercel\.app|https://.*\.txzy\.net",
)

JobStatus = Literal["queued", "running", "completed", "failed", "cancelled"]
TAGS_METADATA = [
    {
        "name": "system",
        "description": "Service health checks and API documentation entry points.",
    },
    {
        "name": "crawls",
        "description": "Create crawl jobs, inspect status, cancel work, and download ZIP outputs.",
    },
]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class CrawlRequest(BaseModel):
    start_url: str = Field(
        min_length=1,
        description="Public documentation start URL to mirror.",
        examples=["https://openrouter.ai/docs/"],
    )
    scope_prefix: str | None = Field(
        default=None,
        description="Optional path prefix to keep the crawl inside a docs subtree, such as /docs/.",
        examples=["/docs/"],
    )
    max_pages: int = Field(
        default=500, ge=1, le=10_000, description="Maximum pages to crawl."
    )
    max_depth: int = Field(
        default=20, ge=0, le=100, description="Maximum crawl depth from the start URL."
    )
    timeout: float = Field(
        default=30.0, gt=0, le=600, description="Per-request timeout in seconds."
    )
    delay: float = Field(
        default=0.0, ge=0, le=60, description="Optional delay between requests."
    )
    workers: int = Field(
        default=5, ge=1, le=64, description="Number of concurrent crawl workers."
    )
    user_agent: str = Field(
        default=DEFAULT_USER_AGENT,
        description="User-Agent header used during crawling.",
    )
    include_sitemaps: bool = Field(
        default=True, description="Whether sitemap discovery should be used."
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "start_url": "https://openrouter.ai/docs/",
                    "scope_prefix": "/docs/",
                    "max_pages": 80,
                    "max_depth": 8,
                    "workers": 6,
                }
            ]
        }
    }


class CrawlPage(BaseModel):
    source_url: str
    final_url: str
    title: str
    output_path: str
    discovered_links: int
    queued_links: int
    status_code: int


class CrawlJobSummary(BaseModel):
    job_id: str
    status: JobStatus
    start_url: str
    scope_prefix: str | None = None
    created_at: str
    started_at: str | None = None
    finished_at: str | None = None
    page_count: int = 0
    skipped_count: int = 0
    error: str | None = None
    manifest_url: str
    archive_url: str
    files_url: str
    cancel_url: str


class CrawlJobDetail(CrawlJobSummary):
    recent_pages: list[CrawlPage] = Field(default_factory=list)
    recent_skipped: list[dict[str, Any]] = Field(default_factory=list)
    manifest: dict[str, Any] | None = None


@dataclass(slots=True)
class JobState:
    job_id: str
    request: CrawlRequest
    job_dir: Path
    content_dir: Path
    archive_path: Path
    request_path: Path
    status: JobStatus = "queued"
    created_at: str = field(default_factory=utc_now_iso)
    started_at: str | None = None
    finished_at: str | None = None
    page_count: int = 0
    skipped_count: int = 0
    error: str | None = None
    report: dict[str, Any] | None = None
    stop_event: threading.Event = field(default_factory=threading.Event)
    lock: threading.Lock = field(default_factory=threading.Lock)
    progress_log: list[dict[str, Any]] = field(default_factory=list)

    def apply_progress(self, event: dict[str, Any]) -> None:
        with self.lock:
            self.progress_log.append(event)
            if event["event"] == "started":
                self.status = "running"
                self.started_at = self.started_at or utc_now_iso()
            elif event["event"] == "page":
                self.page_count = int(event.get("page_count", self.page_count))
                self.skipped_count = int(event.get("skipped_count", self.skipped_count))
            elif event["event"] == "skipped":
                self.skipped_count = int(event.get("skipped_count", self.skipped_count))
            elif event["event"] == "finished":
                self.status = event.get("status", self.status)
                self.page_count = int(event.get("page_count", self.page_count))
                self.skipped_count = int(event.get("skipped_count", self.skipped_count))
                self.finished_at = event.get("finished_at", self.finished_at)

    def snapshot(self) -> dict[str, Any]:
        with self.lock:
            return {
                "job_id": self.job_id,
                "status": self.status,
                "start_url": self.request.start_url,
                "scope_prefix": self.request.scope_prefix,
                "created_at": self.created_at,
                "started_at": self.started_at,
                "finished_at": self.finished_at,
                "page_count": self.page_count,
                "skipped_count": self.skipped_count,
                "error": self.error,
                "recent_pages": self._recent_pages(),
                "recent_skipped": self._recent_skipped(),
                "manifest": self.report,
            }

    def _recent_pages(self) -> list[CrawlPage]:
        if not self.report:
            return []
        pages = self.report.get("pages", [])[-10:]
        return [CrawlPage.model_validate(page) for page in pages]

    def _recent_skipped(self) -> list[dict[str, Any]]:
        if not self.report:
            return []
        return list(self.report.get("skipped", [])[-10:])


class JobManager:
    def __init__(
        self,
        root: Path,
        max_workers: int,
        retention_seconds: int = JOB_RETENTION_SECONDS,
    ) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)
        self._executor = ThreadPoolExecutor(max_workers=max_workers)
        self._jobs: dict[str, JobState] = {}
        self._lock = threading.Lock()
        self.retention_seconds = retention_seconds
        self.cleanup_expired_jobs()

    def close(self) -> None:
        self._executor.shutdown(wait=False, cancel_futures=True)

    def _is_expired(self, value: str | None) -> bool:
        if not value:
            return False
        try:
            timestamp = datetime.fromisoformat(value)
        except ValueError:
            return False
        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=timezone.utc)
        age_seconds = (datetime.now(timezone.utc) - timestamp).total_seconds()
        return age_seconds >= self.retention_seconds

    def cleanup_expired_jobs(self) -> None:
        stale_job_dirs: list[Path] = []

        with self._lock:
            for job_id, state in list(self._jobs.items()):
                marker = state.finished_at or state.created_at
                if state.status in {
                    "completed",
                    "failed",
                    "cancelled",
                } and self._is_expired(marker):
                    stale_job_dirs.append(state.job_dir)
                    self._jobs.pop(job_id, None)

        for job_dir in stale_job_dirs:
            shutil.rmtree(job_dir, ignore_errors=True)

        for path in self.root.iterdir():
            if not path.is_dir():
                continue
            try:
                modified_at = datetime.fromtimestamp(
                    path.stat().st_mtime, tz=timezone.utc
                )
            except OSError:
                continue
            if (
                datetime.now(timezone.utc) - modified_at
            ).total_seconds() >= self.retention_seconds:
                shutil.rmtree(path, ignore_errors=True)

    def create_job(self, request: CrawlRequest) -> JobState:
        self.cleanup_expired_jobs()
        job_id = uuid.uuid4().hex
        job_dir = self.root / job_id
        content_dir = job_dir / "content"
        archive_path = job_dir / "archive.zip"
        request_path = job_dir / "request.json"
        content_dir.mkdir(parents=True, exist_ok=True)
        state = JobState(
            job_id=job_id,
            request=request,
            job_dir=job_dir,
            content_dir=content_dir,
            archive_path=archive_path,
            request_path=request_path,
        )
        request_path.write_text(
            json.dumps(request.model_dump(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        with self._lock:
            self._jobs[job_id] = state
        self._executor.submit(self._run_job, job_id)
        return state

    def get(self, job_id: str) -> JobState:
        with self._lock:
            state = self._jobs.get(job_id)
        if state is None:
            raise KeyError(job_id)
        return state

    def cancel(self, job_id: str) -> JobState:
        state = self.get(job_id)
        state.stop_event.set()
        with state.lock:
            if state.status == "queued":
                state.status = "cancelled"
        return state

    def _run_job(self, job_id: str) -> None:
        state = self.get(job_id)
        state.started_at = state.started_at or utc_now_iso()
        state.status = "running"

        def on_progress(event: dict[str, Any]) -> None:
            state.apply_progress(event)

        try:
            report = crawl_docs(
                state.request.start_url,
                state.content_dir,
                max_pages=state.request.max_pages,
                max_depth=state.request.max_depth,
                timeout=state.request.timeout,
                delay=state.request.delay,
                workers=state.request.workers,
                user_agent=state.request.user_agent,
                scope_prefix=state.request.scope_prefix,
                include_sitemaps=state.request.include_sitemaps,
                progress_callback=on_progress,
                stop_event=state.stop_event,
            )
            state.report = build_manifest(report)
            state.page_count = report.page_count
            state.skipped_count = report.skipped_count
            state.finished_at = report.finished_at
            state.status = report.status
            self._write_archive(state)
            self.cleanup_expired_jobs()
        except Exception as exc:  # pragma: no cover - surfaced through API state
            logger.exception("Job %s failed", job_id)
            state.error = str(exc)
            state.status = "failed"
            state.finished_at = utc_now_iso()
            self.cleanup_expired_jobs()

    def _write_archive(self, state: JobState) -> None:
        state.archive_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(
            state.archive_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
        ) as archive:
            for path in state.content_dir.rglob("*"):
                if path.is_file():
                    archive.write(
                        path,
                        arcname=path.relative_to(state.content_dir).as_posix(),
                    )


def safe_resolve(base: Path, candidate: str) -> Path:
    resolved = (base / candidate).resolve()
    base_resolved = base.resolve()
    if base_resolved not in resolved.parents and resolved != base_resolved:
        raise HTTPException(status_code=400, detail="Invalid path")
    return resolved


def job_urls(job_id: str) -> dict[str, str]:
    return {
        "manifest_url": f"/v1/crawls/{job_id}/manifest",
        "archive_url": f"/v1/crawls/{job_id}/archive",
        "files_url": f"/v1/crawls/{job_id}/files",
        "cancel_url": f"/v1/crawls/{job_id}/cancel",
    }


def public_summary(state: JobState) -> CrawlJobSummary:
    payload = {
        "job_id": state.job_id,
        "status": state.status,
        "start_url": state.request.start_url,
        "scope_prefix": state.request.scope_prefix,
        "created_at": state.created_at,
        "started_at": state.started_at,
        "finished_at": state.finished_at,
        "page_count": state.page_count,
        "skipped_count": state.skipped_count,
        "error": state.error,
        **job_urls(state.job_id),
    }
    return CrawlJobSummary.model_validate(payload)


def public_detail(state: JobState) -> CrawlJobDetail:
    snapshot = state.snapshot()
    payload = {
        **public_summary(state).model_dump(),
        "recent_pages": snapshot["recent_pages"],
        "recent_skipped": snapshot["recent_skipped"],
        "manifest": snapshot["manifest"],
    }
    return CrawlJobDetail.model_validate(payload)


@asynccontextmanager
async def lifespan(_: FastAPI):
    try:
        manager = JobManager(DATA_ROOT, MAX_JOB_WORKERS, JOB_RETENTION_SECONDS)
    except OSError as exc:
        logger.error("Failed to initialise JobManager at %s: %s", DATA_ROOT, exc)
        manager = JobManager(
            Path("/tmp/doc_getter_runs"), MAX_JOB_WORKERS, JOB_RETENTION_SECONDS
        )
    app.state.job_manager = manager
    try:
        yield
    finally:
        manager.close()


app = FastAPI(
    title="Doc Getter API",
    summary="Submit a docs URL, crawl it asynchronously, and download a ZIP archive.",
    description=(
        "Async API for the `doc_getter` service.\n\n"
        "## Typical flow\n"
        "1. `POST /v1/crawls` with a `start_url`\n"
        "2. Poll `GET /v1/crawls/{job_id}` until status becomes `completed`\n"
        "3. Download the result from `GET /v1/crawls/{job_id}/archive`\n\n"
        f"Generated files are temporary and are cleaned up automatically after about {JOB_RETENTION_SECONDS} seconds."
    ),
    version="0.1.0",
    lifespan=lifespan,
    openapi_tags=TAGS_METADATA,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    swagger_ui_parameters={
        "displayRequestDuration": True,
        "docExpansion": "list",
        "defaultModelsExpandDepth": 2,
    },
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_origin_regex=CORS_ALLOW_ORIGIN_REGEX,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["system"], summary="API index")
def index() -> dict[str, Any]:
    return {
        "name": "doc_getter service",
        "status": "ok",
        "docs": "/docs",
        "redoc": "/redoc",
        "openapi": "/openapi.json",
        "healthz": "/healthz",
        "retention_seconds": JOB_RETENTION_SECONDS,
    }


@app.get("/healthz", tags=["system"], summary="Health check")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/v1/crawls",
    response_model=CrawlJobSummary,
    status_code=202,
    tags=["crawls"],
    summary="Create a crawl job",
    description="Submit a public docs URL and start an asynchronous crawl job.",
)
def create_crawl(request: CrawlRequest) -> CrawlJobSummary:
    manager: JobManager = app.state.job_manager
    state = manager.create_job(request)
    return public_summary(state)


@app.get(
    "/v1/crawls/{job_id}",
    response_model=CrawlJobDetail,
    tags=["crawls"],
    summary="Get crawl job status",
    description="Poll a job until it reaches `completed`, `failed`, or `cancelled`.",
)
def get_crawl(job_id: str) -> CrawlJobDetail:
    manager: JobManager = app.state.job_manager
    try:
        state = manager.get(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc
    return public_detail(state)


@app.post(
    "/v1/crawls/{job_id}/cancel",
    response_model=CrawlJobSummary,
    tags=["crawls"],
    summary="Cancel a crawl job",
)
def cancel_crawl(job_id: str) -> CrawlJobSummary:
    manager: JobManager = app.state.job_manager
    try:
        state = manager.cancel(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc
    return public_summary(state)


@app.get(
    "/v1/crawls/{job_id}/manifest",
    tags=["crawls"],
    summary="Get the crawl manifest",
)
def get_manifest(job_id: str) -> dict[str, Any]:
    manager: JobManager = app.state.job_manager
    try:
        state = manager.get(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc
    if state.report is None:
        raise HTTPException(status_code=409, detail="Manifest is not ready yet")
    return state.report


@app.get(
    "/v1/crawls/{job_id}/archive",
    tags=["crawls"],
    summary="Download the ZIP archive",
)
def get_archive(job_id: str) -> FileResponse:
    manager: JobManager = app.state.job_manager
    try:
        state = manager.get(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc
    if not state.archive_path.exists():
        raise HTTPException(status_code=409, detail="Archive is not ready yet")
    return FileResponse(
        state.archive_path,
        media_type="application/zip",
        filename=f"{job_id}.zip",
    )


@app.get(
    "/v1/crawls/{job_id}/files",
    tags=["crawls"],
    summary="List generated files",
)
def list_files(job_id: str) -> dict[str, Any]:
    manager: JobManager = app.state.job_manager
    try:
        state = manager.get(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc

    files: list[dict[str, Any]] = []
    if state.content_dir.exists():
        for path in sorted(state.content_dir.rglob("*")):
            if path.is_file():
                files.append(
                    {
                        "path": path.relative_to(state.content_dir).as_posix(),
                        "size": path.stat().st_size,
                    }
                )
    return {"job_id": job_id, "files": files}


@app.get(
    "/v1/crawls/{job_id}/files/{relative_path:path}",
    tags=["crawls"],
    summary="Download one generated file",
)
def get_file(job_id: str, relative_path: str) -> FileResponse:
    manager: JobManager = app.state.job_manager
    try:
        state = manager.get(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc
    target = safe_resolve(state.content_dir, relative_path)
    if not target.exists() or not target.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(target)


def main() -> None:
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("service:app", host="0.0.0.0", port=port, reload=False)


if __name__ == "__main__":
    main()
