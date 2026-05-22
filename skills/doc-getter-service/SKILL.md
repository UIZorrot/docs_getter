---
name: doc-getter-service
description: Expose and extend the doc_getter crawler as a public docs-to-ZIP service with a Next.js frontend (`getdoc.tool.txzy.net`) and a FastAPI backend (`api.tool.getdoc.txzy.net`). Use when asked to add or modify crawl APIs, Swagger/OpenAPI docs, async job polling, ZIP download flows, temporary file cleanup, deployment behavior, or the one-field public UI where users only submit a docs URL.
---

# Doc Getter Service

Use this skill when the task is about the hosted doc getter product rather than the local-only crawler script.

## Hosted service defaults

- **Frontend:** `https://getdoc.tool.txzy.net`
- **Backend API:** `https://api.tool.getdoc.txzy.net`
- **Swagger UI:** `https://api.tool.getdoc.txzy.net/docs`
- Public UX should prefer **one required input only**: the docs URL.
- Each request should run in an isolated temporary job directory and expose a ZIP download when complete.
- Old job artifacts should be cleaned up automatically after the retention window.

## Core workflow

1. Keep crawl logic in the shared crawler module.
2. Put service-specific behavior in `service.py`.
3. Expose jobs instead of blocking requests.
4. Persist each crawl under a job directory so callers can poll, download, or inspect results later.

## Preferred API shape

- `POST /v1/crawls` to create a job
- `GET /v1/crawls/{job_id}` to poll job status and progress
- `POST /v1/crawls/{job_id}/cancel` to stop a running job
- `GET /v1/crawls/{job_id}/manifest` to fetch the crawl manifest JSON
- `GET /v1/crawls/{job_id}/archive` to download a ZIP of generated Markdown
- `GET /v1/crawls/{job_id}/files` to list generated files
- `GET /v1/crawls/{job_id}/files/{path}` to fetch one generated file
- `GET /docs` to expose Swagger UI for public API consumers

## Implementation rules

- Keep the crawler CLI working even after adding the API.
- Treat `crawl_docs(..., progress_callback=..., stop_event=...)` as the integration point for status updates and cancellation.
- Update manifest fields and API models together when the output schema changes.
- Store job artifacts in a server-managed directory such as `runs/<job_id>/`.
- Prefer returning download URLs and status URLs over raw filesystem paths.

## When editing service code

- Update request validation in the FastAPI model and the job summary response together.
- If adding a new output, include it in the manifest, archive, and file-listing behavior.
- If changing crawl lifecycle, make sure queued, running, completed, failed, and cancelled states remain distinct.
