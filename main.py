from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
import argparse
import concurrent.futures
import json
import logging
import os
import re
import threading
import time
from pathlib import Path, PurePosixPath
from typing import Any, Callable
from urllib.parse import urljoin, urlsplit, urlunsplit, unquote
from xml.etree import ElementTree as ET

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_markdown

logger = logging.getLogger(__name__)
_thread_local = threading.local()

try:
    from scrapling.parser import Selector
except Exception:  # pragma: no cover - optional dependency fallback
    Selector = None


DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)
HTML_TYPES = {"text/html", "application/xhtml+xml"}
SKIP_TAGS = {
    "script",
    "style",
    "noscript",
    "svg",
    "canvas",
    "iframe",
    "object",
    "embed",
    "form",
    "button",
}
CONTENT_SELECTORS = (
    "article",
    '[role="main"]',
    "[data-page-content]",
    "[data-content]",
    "main",
)
WINDOWS_INVALID_PATH_CHARS = re.compile(r'[<>:"/\\\\|?*\x00-\x1f]')


@dataclass(slots=True)
class PageRecord:
    source_url: str
    final_url: str
    title: str
    output_path: str
    discovered_links: int
    queued_links: int
    status_code: int


@dataclass(slots=True)
class CrawlReport:
    start_url: str
    output_dir: Path
    site_dir: Path
    scope_prefix: str
    pages: list[PageRecord] = field(default_factory=list)
    skipped: list[dict[str, Any]] = field(default_factory=list)
    status: str = "completed"
    started_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    finished_at: str | None = None

    @property
    def page_count(self) -> int:
        return len(self.pages)

    @property
    def skipped_count(self) -> int:
        return len(self.skipped)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


ProgressCallback = Callable[[dict[str, Any]], None]


def emit_progress(
    progress_callback: ProgressCallback | None,
    event: str,
    **payload: Any,
) -> None:
    if progress_callback is None:
        return
    try:
        progress_callback({"event": event, **payload})
    except Exception:
        logger.debug("Progress callback raised an exception", exc_info=True)


def clean_segment(segment: str) -> str:
    value = unquote(segment).strip()
    value = WINDOWS_INVALID_PATH_CHARS.sub("_", value)
    value = value.rstrip(". ")
    if value in {"", ".", ".."}:
        return "_"
    return value


def normalize_url(url: str, keep_query: bool = False) -> str:
    parsed = urlsplit(url)
    scheme = parsed.scheme.lower() or "https"
    netloc = parsed.netloc.lower()
    path = parsed.path or "/"
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    query = parsed.query if keep_query else ""
    fragment = ""
    return urlunsplit((scheme, netloc, path, query, fragment))


def same_scope(url: str, base_host: str, scope_prefix: str) -> bool:
    parsed = urlsplit(url)
    if parsed.netloc.lower() != base_host.lower():
        return False
    path = parsed.path or "/"
    if scope_prefix == "/":
        return True
    if path == scope_prefix.rstrip("/"):
        return True
    return path.startswith(scope_prefix)


def infer_scope_prefix(start_url: str) -> str:
    path = urlsplit(start_url).path or "/"
    if path == "/":
        return "/"
    parts = [part for part in path.split("/") if part]
    if "docs" in parts:
        idx = parts.index("docs")
        return "/" + "/".join(parts[: idx + 1]) + "/"
    if len(parts) == 1:
        return "/"
    return "/" + parts[0] + "/"


def safe_host_dir(hostname: str) -> str:
    return clean_segment(hostname)


def url_to_output_path(url: str, site_dir: Path) -> Path:
    parsed = urlsplit(url)
    path = parsed.path or "/"
    if path == "/":
        return site_dir / "index.md"

    parts = [clean_segment(part) for part in path.split("/") if part]
    if not parts:
        return site_dir / "index.md"

    last = parts[-1]
    suffix = PurePosixPath(last).suffix.lower()
    if path.endswith("/") or not suffix:
        return site_dir.joinpath(*parts, "index.md")

    if suffix in {".html", ".htm", ".xhtml"}:
        parts[-1] = PurePosixPath(last).with_suffix(".md").name
        return site_dir.joinpath(*parts)

    return site_dir.joinpath(*parts, "index.md")


def output_path_to_url(path: Path, site_dir: Path, base_url: str) -> str:
    relative = path.relative_to(site_dir)
    parts = list(relative.parts)
    if not parts:
        return base_url

    if parts[-1] == "index.md":
        parts = parts[:-1]
        rel_path = "/".join(parts)
        if rel_path:
            return urljoin(base_url.rstrip("/") + "/", rel_path.rstrip("/") + "/")
        return base_url.rstrip("/") + "/"

    if parts[-1].lower().endswith(".md"):
        rel_path = "/".join(
            parts[:-1] + [PurePosixPath(parts[-1]).with_suffix("").name]
        )
        return urljoin(base_url.rstrip("/") + "/", rel_path)

    rel_path = "/".join(parts)
    return urljoin(base_url.rstrip("/") + "/", rel_path)


def select_fragment_html(html: str) -> str:
    if Selector is not None:
        try:
            selector = Selector(html)
            for css in CONTENT_SELECTORS:
                try:
                    matches = selector.css(css)
                except Exception:
                    continue
                if matches:
                    first = matches[0]
                    fragment = getattr(first, "html_content", None)
                    if fragment:
                        return fragment
        except Exception:
            pass

    soup = BeautifulSoup(html, "lxml")
    for css in CONTENT_SELECTORS:
        container = soup.select_one(css)
        if container is not None:
            return str(container)
    body = soup.body
    if body is not None:
        return str(body)
    return html


def prune_fragment_html(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup.find_all(list(SKIP_TAGS)):
        tag.decompose()
    return str(soup)


def extract_page_title(html: str) -> str:
    if Selector is not None:
        try:
            selector = Selector(html)
            title = selector.css("title::text").get("")
            if title.strip():
                return title.strip()
        except Exception:
            pass

    soup = BeautifulSoup(html, "lxml")
    if soup.title and soup.title.text.strip():
        return soup.title.text.strip()
    h1 = soup.find("h1")
    if h1 and h1.get_text(" ", strip=True):
        return h1.get_text(" ", strip=True)
    return "Untitled page"


def extract_hrefs(html: str) -> list[str]:
    if Selector is not None:
        try:
            selector = Selector(html)
            return [
                href.strip()
                for href in selector.css("a[href]::attr(href)").getall()
                if href and href.strip()
            ]
        except Exception:
            pass

    soup = BeautifulSoup(html, "lxml")
    return [
        href.strip()
        for href in (a.get("href") for a in soup.find_all("a", href=True))
        if href
    ]


def fetch_html(
    session: requests.Session, url: str, timeout: float, user_agent: str
) -> tuple[str, requests.Response]:
    response = session.get(
        url,
        timeout=timeout,
        headers={
            "User-Agent": user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        },
        allow_redirects=True,
    )
    response.raise_for_status()
    if response.encoding is None:
        response.encoding = response.apparent_encoding or "utf-8"
    return response.text, response


def looks_like_html(response: requests.Response) -> bool:
    content_type = (
        response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
    )
    if not content_type:
        return True
    return content_type in HTML_TYPES or content_type.endswith("+xml")


def _thread_fetch(
    url: str, timeout: float, user_agent: str
) -> tuple[str, requests.Response]:
    """Fetch a page using a per-thread session for safe concurrent use."""
    if not hasattr(_thread_local, "session"):
        _thread_local.session = requests.Session()
    return fetch_html(_thread_local.session, url, timeout, user_agent)


def discover_robots_sitemaps(
    session: requests.Session, base_url: str, timeout: float, user_agent: str
) -> list[str]:
    robots_url = urljoin(base_url.rstrip("/") + "/", "/robots.txt")
    try:
        logger.info(f"Checking robots.txt at {robots_url}")
        response = session.get(
            robots_url, timeout=timeout, headers={"User-Agent": user_agent}
        )
        if response.status_code >= 400:
            logger.debug(f"robots.txt not found (status: {response.status_code})")
            return []
        response.encoding = response.encoding or response.apparent_encoding or "utf-8"
    except requests.RequestException as e:
        logger.debug(f"Failed to fetch robots.txt: {e}")
        return []

    sitemaps: list[str] = []
    for raw_line in response.text.splitlines():
        line = raw_line.strip()
        if not line.lower().startswith("sitemap:"):
            continue
        candidate = line.split(":", 1)[1].strip()
        if candidate:
            sitemaps.append(candidate)
            logger.debug(f"Found sitemap: {candidate}")
    return sitemaps


def parse_sitemap_xml(
    session: requests.Session, sitemap_url: str, timeout: float, user_agent: str
) -> set[str]:
    discovered: set[str] = set()
    pending = deque([sitemap_url])
    seen_sitemaps: set[str] = set()
    logger.debug(f"Starting to parse sitemap: {sitemap_url}")

    while pending:
        current = normalize_url(pending.popleft(), keep_query=False)
        if current in seen_sitemaps:
            continue
        seen_sitemaps.add(current)
        try:
            response = session.get(
                current, timeout=timeout, headers={"User-Agent": user_agent}
            )
            response.raise_for_status()
        except requests.RequestException as e:
            logger.debug(f"Failed to fetch sitemap {current}: {e}")
            continue

        try:
            root = ET.fromstring(response.text)
        except ET.ParseError as e:
            logger.debug(f"Failed to parse sitemap {current}: {e}")
            continue

        tag = root.tag.lower()
        if tag.endswith("sitemapindex"):
            for node in root.iter():
                if node.tag.lower().endswith("loc") and node.text:
                    pending.append(node.text.strip())
            logger.debug(f"Found sitemap index with {len(pending)} child sitemaps")
            continue

        for node in root.iter():
            if node.tag.lower().endswith("loc") and node.text:
                discovered.add(node.text.strip())

    logger.info(f"Discovered {len(discovered)} URLs from sitemaps")
    return discovered


def discover_seed_urls(
    session: requests.Session,
    start_url: str,
    timeout: float,
    user_agent: str,
    include_sitemaps: bool,
) -> set[str]:
    seeds = {normalize_url(start_url)}
    if not include_sitemaps:
        logger.info("Sitemap discovery disabled, using only start URL")
        return seeds

    parsed = urlsplit(start_url)
    site_root = f"{parsed.scheme}://{parsed.netloc}"
    logger.info(f"Discovering seed URLs for {site_root}")
    sitemap_candidates = discover_robots_sitemaps(
        session, site_root, timeout, user_agent
    )
    if not sitemap_candidates:
        logger.debug("No sitemaps found in robots.txt, trying /sitemap.xml")
        sitemap_candidates = [urljoin(site_root + "/", "sitemap.xml")]

    for sitemap_url in sitemap_candidates:
        for candidate in parse_sitemap_xml(session, sitemap_url, timeout, user_agent):
            seeds.add(normalize_url(candidate))

    logger.info(f"Total seed URLs discovered: {len(seeds)}")
    return seeds


def is_probably_html_url(url: str) -> bool:
    path = urlsplit(url).path.lower()
    if not path:
        return True
    return not path.endswith(
        (
            ".pdf",
            ".zip",
            ".png",
            ".jpg",
            ".jpeg",
            ".gif",
            ".webp",
            ".svg",
            ".mp4",
            ".mp3",
        )
    )


def rewrite_internal_links(
    html: str,
    current_url: str,
    current_output_path: Path,
    site_dir: Path,
    base_host: str,
    scope_prefix: str,
) -> tuple[str, list[str]]:
    soup = BeautifulSoup(html, "lxml")
    discovered_links: list[str] = []

    for anchor in soup.find_all("a", href=True):
        raw_href = anchor.get("href", "").strip()
        if not raw_href or raw_href.startswith(("javascript:", "mailto:", "tel:")):
            continue
        target = normalize_url(urljoin(current_url, raw_href))
        if target == normalize_url(current_url):
            fragment = urlsplit(raw_href).fragment
            if fragment:
                anchor["href"] = f"#{fragment}"
            else:
                anchor["href"] = current_output_path.name
            continue

        if not same_scope(target, base_host, scope_prefix) or not is_probably_html_url(
            target
        ):
            anchor["href"] = target
            continue

        target_output = url_to_output_path(target, site_dir)
        rel_href = os.path.relpath(
            str(target_output), start=str(current_output_path.parent)
        )
        anchor["href"] = rel_href.replace("\\", "/")
        discovered_links.append(target)

    return str(soup), discovered_links


def html_to_page_markdown(
    html: str,
    current_url: str,
    current_output_path: Path,
    site_dir: Path,
    base_host: str,
    scope_prefix: str,
) -> tuple[str, str, list[str]]:
    fragment = prune_fragment_html(select_fragment_html(html))
    rewritten_fragment, discovered_links = rewrite_internal_links(
        fragment,
        current_url=current_url,
        current_output_path=current_output_path,
        site_dir=site_dir,
        base_host=base_host,
        scope_prefix=scope_prefix,
    )
    title = extract_page_title(html)
    markdown_body = html_to_markdown(
        rewritten_fragment,
        heading_style="ATX",
        bullets="-",
        strip=["span"],
        autolinks=False,
    )
    markdown_body = markdown_body.replace("\r\n", "\n").replace("\r", "\n")
    markdown_body = re.sub(r"\n{3,}", "\n\n", markdown_body).strip()
    front_matter = "\n".join(
        [
            "---",
            f"source_url: {json.dumps(current_url, ensure_ascii=False)}",
            f"title: {json.dumps(title, ensure_ascii=False)}",
            f"crawled_at: {json.dumps(utc_now_iso(), ensure_ascii=False)}",
            "---",
            "",
        ]
    )
    return front_matter + markdown_body + "\n", title, discovered_links


def write_page(path: Path, markdown: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown, encoding="utf-8", newline="\n")


def build_manifest(report: CrawlReport) -> dict[str, Any]:
    return {
        "start_url": report.start_url,
        "output_dir": str(report.output_dir),
        "site_dir": str(report.site_dir),
        "scope_prefix": report.scope_prefix,
        "status": report.status,
        "started_at": report.started_at,
        "finished_at": report.finished_at,
        "page_count": report.page_count,
        "skipped_count": report.skipped_count,
        "pages": [
            {
                "source_url": page.source_url,
                "final_url": page.final_url,
                "title": page.title,
                "output_path": page.output_path,
                "discovered_links": page.discovered_links,
                "queued_links": page.queued_links,
                "status_code": page.status_code,
            }
            for page in report.pages
        ],
        "skipped": report.skipped,
    }


def write_manifest(report: CrawlReport) -> None:
    manifest_path = report.site_dir / "_mirror-manifest.json"
    manifest_path.write_text(
        json.dumps(build_manifest(report), ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )


def crawl_docs(
    start_url: str,
    output_dir: Path,
    *,
    max_pages: int = 500,
    max_depth: int = 20,
    timeout: float = 30.0,
    delay: float = 0.0,
    workers: int = 5,
    user_agent: str = DEFAULT_USER_AGENT,
    scope_prefix: str | None = None,
    include_sitemaps: bool = True,
    progress_callback: ProgressCallback | None = None,
    stop_event: threading.Event | None = None,
) -> CrawlReport:
    seed_session = requests.Session()
    normalized_start = normalize_url(start_url)
    parsed = urlsplit(normalized_start)
    base_host = parsed.netloc
    effective_scope = scope_prefix or infer_scope_prefix(normalized_start)
    site_dir = output_dir

    logger.info(f"Starting crawl: {normalized_start}")
    logger.info(f"Output directory: {site_dir}")
    logger.info(f"Scope prefix: {effective_scope}")
    logger.info(f"Max pages: {max_pages}, Max depth: {max_depth}, Workers: {workers}")
    emit_progress(
        progress_callback,
        "started",
        start_url=normalized_start,
        output_dir=str(site_dir),
        scope_prefix=effective_scope,
        max_pages=max_pages,
        max_depth=max_depth,
        workers=workers,
    )

    report = CrawlReport(
        start_url=normalized_start,
        output_dir=output_dir,
        site_dir=site_dir,
        scope_prefix=effective_scope,
    )

    queue: deque[tuple[str, int]] = deque()
    queued: set[str] = set()
    seen: set[str] = set()

    def enqueue(candidate: str, depth: int) -> None:
        if stop_event is not None and stop_event.is_set():
            return
        normalized = normalize_url(candidate)
        if normalized in seen or normalized in queued:
            return
        if not same_scope(normalized, base_host, effective_scope):
            return
        if not is_probably_html_url(normalized):
            return
        queue.append((normalized, depth))
        queued.add(normalized)
        logger.debug(f"Queued (depth {depth}): {normalized}")

    for seed in sorted(
        discover_seed_urls(
            seed_session,
            normalized_start,
            timeout=timeout,
            user_agent=user_agent,
            include_sitemaps=include_sitemaps,
        )
    ):
        enqueue(seed, 0)

    if not queue:
        logger.info("No seed URLs found, using start URL only")
        enqueue(normalized_start, 0)

    logger.info(f"Starting crawl with {len(queue)} initial URLs")

    in_flight: dict[concurrent.futures.Future, tuple[str, int]] = {}

    def submit_pending(executor: concurrent.futures.ThreadPoolExecutor) -> None:
        if stop_event is not None and stop_event.is_set():
            return
        while (
            queue
            and (report.page_count + len(in_flight)) < max_pages
            and len(in_flight) < workers
            and (stop_event is None or not stop_event.is_set())
        ):
            url, depth = queue.popleft()
            queued.discard(url)
            if url in seen:
                continue
            seen.add(url)
            future = executor.submit(_thread_fetch, url, timeout, user_agent)
            in_flight[future] = (url, depth)

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        submit_pending(executor)

        while in_flight:
            done, _ = concurrent.futures.wait(
                in_flight, return_when=concurrent.futures.FIRST_COMPLETED
            )

            for future in done:
                url, depth = in_flight.pop(future)

                try:
                    html, response = future.result()
                except requests.RequestException as exc:
                    logger.warning(f"Failed to fetch {url}: {exc}")
                    report.skipped.append({"url": url, "error": str(exc)})
                    emit_progress(
                        progress_callback,
                        "skipped",
                        url=url,
                        error=str(exc),
                        skipped_count=report.skipped_count,
                    )
                    continue

                if not looks_like_html(response):
                    content_type = response.headers.get("content-type", "unknown")
                    logger.debug(f"Skipped non-HTML {url} ({content_type})")
                    report.skipped.append(
                        {
                            "url": url,
                            "error": f"Skipped non-HTML response ({content_type})",
                        }
                    )
                    emit_progress(
                        progress_callback,
                        "skipped",
                        url=url,
                        error=f"Skipped non-HTML response ({content_type})",
                        skipped_count=report.skipped_count,
                    )
                    continue

                final_url = normalize_url(response.url)
                # Redirect dedup: if the server redirected us, mark the final URL
                # as seen so it won't be fetched again if it appears in the queue.
                if final_url != url:
                    logger.debug(f"Redirect: {url} -> {final_url}")
                    seen.add(final_url)
                    queued.discard(final_url)

                current_output_path = url_to_output_path(final_url, site_dir)

                logger.info(
                    f"[{report.page_count + 1}/{max_pages}] {final_url}"
                    f" (queue={len(queue)}, in-flight={len(in_flight)})"
                )

                markdown, title, discovered_links = html_to_page_markdown(
                    html,
                    current_url=final_url,
                    current_output_path=current_output_path,
                    site_dir=site_dir,
                    base_host=base_host,
                    scope_prefix=effective_scope,
                )
                write_page(current_output_path, markdown)
                logger.debug(f"Wrote: {current_output_path.relative_to(site_dir)}")

                queued_count = 0
                if depth < max_depth:
                    for link in discovered_links:
                        before = len(queue)
                        enqueue(link, depth + 1)
                        if len(queue) > before:
                            queued_count += 1

                report.pages.append(
                    PageRecord(
                        source_url=url,
                        final_url=final_url,
                        title=title,
                        output_path=str(
                            current_output_path.relative_to(site_dir)
                        ).replace("\\", "/"),
                        discovered_links=len(discovered_links),
                        queued_links=queued_count,
                        status_code=response.status_code,
                    )
                )
                emit_progress(
                    progress_callback,
                    "page",
                    source_url=url,
                    final_url=final_url,
                    output_path=report.pages[-1].output_path,
                    title=title,
                    page_count=report.page_count,
                    skipped_count=report.skipped_count,
                    queued_count=len(queue),
                )

                logger.debug(
                    f"Depth {depth}: found {len(discovered_links)} links, queued {queued_count} new"
                )

            if delay > 0 and done:
                time.sleep(delay)

            if stop_event is not None and stop_event.is_set():
                break

            submit_pending(executor)

    report.finished_at = utc_now_iso()
    report.status = "cancelled" if stop_event is not None and stop_event.is_set() else "completed"
    write_manifest(report)
    logger.info(
        f"Crawl complete. Pages written: {report.page_count}, Skipped: {report.skipped_count}"
    )
    emit_progress(
        progress_callback,
        "finished",
        status=report.status,
        page_count=report.page_count,
        skipped_count=report.skipped_count,
        finished_at=report.finished_at,
    )
    return report


def format_report(report: CrawlReport) -> str:
    lines = [
        f"Start URL: {report.start_url}",
        f"Site dir: {report.site_dir}",
        f"Scope prefix: {report.scope_prefix}",
        f"Status: {report.status}",
        f"Pages written: {report.page_count}",
        f"Skipped: {report.skipped_count}",
    ]
    if report.pages:
        lines.append("Recent pages:")
        for page in report.pages[-5:]:
            lines.append(f"  - {page.output_path} <- {page.final_url}")
    if report.skipped:
        lines.append("Skipped URLs:")
        for item in report.skipped[-5:]:
            lines.append(f"  - {item['url']}: {item['error']}")
    return "\n".join(lines)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Mirror a docs site into local Markdown files.",
    )
    parser.add_argument(
        "start_url", help="Starting page, such as https://openrouter.ai/docs/"
    )
    parser.add_argument(
        "--output",
        default="docs",
        help="Output directory. The crawler will create a subfolder named after the host.",
    )
    parser.add_argument(
        "--scope-prefix",
        default=None,
        help="Limit crawling to paths under this prefix, for example /docs/ . Defaults to an inferred scope.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=500,
        help="Maximum number of pages to write (default: 500).",
    )
    parser.add_argument(
        "--max-depth", type=int, default=20, help="Maximum link depth to follow."
    )
    parser.add_argument(
        "--timeout", type=float, default=30.0, help="Request timeout in seconds."
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Delay between page fetches in seconds.",
    )
    parser.add_argument(
        "--user-agent", default=DEFAULT_USER_AGENT, help="Custom User-Agent header."
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=5,
        help="Number of concurrent page fetches (default: 5).",
    )
    parser.add_argument(
        "--no-sitemaps",
        action="store_true",
        help="Do not seed the crawl from robots.txt or sitemap.xml.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose (debug) logging.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    report = crawl_docs(
        args.start_url,
        Path(args.output),
        max_pages=args.max_pages,
        max_depth=args.max_depth,
        timeout=args.timeout,
        delay=args.delay,
        workers=args.workers,
        user_agent=args.user_agent,
        scope_prefix=args.scope_prefix,
        include_sitemaps=not args.no_sitemaps,
    )
    print(format_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

