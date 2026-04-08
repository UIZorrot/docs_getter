from __future__ import annotations

import json
import logging
import os
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
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from main import DEFAULT_USER_AGENT, build_manifest, crawl_docs

logger = logging.getLogger(__name__)

DATA_ROOT = Path(os.getenv("DOC_GETTER_DATA_DIR", "runs")).resolve()
MAX_JOB_WORKERS = max(2, int(os.getenv("DOC_GETTER_JOB_WORKERS", "4")))

JobStatus = Literal["queued", "running", "completed", "failed", "cancelled"]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class CrawlRequest(BaseModel):
    start_url: str = Field(min_length=1)
    scope_prefix: str | None = None
    max_pages: int = Field(default=500, ge=1, le=10_000)
    max_depth: int = Field(default=20, ge=0, le=100)
    timeout: float = Field(default=30.0, gt=0, le=600)
    delay: float = Field(default=0.0, ge=0, le=60)
    workers: int = Field(default=5, ge=1, le=64)
    user_agent: str = DEFAULT_USER_AGENT
    include_sitemaps: bool = True


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
    def __init__(self, root: Path, max_workers: int) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)
        self._executor = ThreadPoolExecutor(max_workers=max_workers)
        self._jobs: dict[str, JobState] = {}
        self._lock = threading.Lock()

    def close(self) -> None:
        self._executor.shutdown(wait=False, cancel_futures=True)

    def create_job(self, request: CrawlRequest) -> JobState:
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
        except Exception as exc:  # pragma: no cover - surfaced through API state
            logger.exception("Job %s failed", job_id)
            state.error = str(exc)
            state.status = "failed"
            state.finished_at = utc_now_iso()

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
    manager = JobManager(DATA_ROOT, MAX_JOB_WORKERS)
    app.state.job_manager = manager
    try:
        yield
    finally:
        manager.close()


app = FastAPI(
    title="doc_getter service",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/crawls", response_model=CrawlJobSummary, status_code=202)
def create_crawl(request: CrawlRequest) -> CrawlJobSummary:
    manager: JobManager = app.state.job_manager
    state = manager.create_job(request)
    return public_summary(state)


@app.get("/v1/crawls/{job_id}", response_model=CrawlJobDetail)
def get_crawl(job_id: str) -> CrawlJobDetail:
    manager: JobManager = app.state.job_manager
    try:
        state = manager.get(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc
    return public_detail(state)


@app.post("/v1/crawls/{job_id}/cancel", response_model=CrawlJobSummary)
def cancel_crawl(job_id: str) -> CrawlJobSummary:
    manager: JobManager = app.state.job_manager
    try:
        state = manager.cancel(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc
    return public_summary(state)


@app.get("/v1/crawls/{job_id}/manifest")
def get_manifest(job_id: str) -> dict[str, Any]:
    manager: JobManager = app.state.job_manager
    try:
        state = manager.get(job_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Job not found") from exc
    if state.report is None:
        raise HTTPException(status_code=409, detail="Manifest is not ready yet")
    return state.report


@app.get("/v1/crawls/{job_id}/archive")
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


@app.get("/v1/crawls/{job_id}/files")
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


@app.get("/v1/crawls/{job_id}/files/{relative_path:path}")
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
    uvicorn.run("service:app", host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
