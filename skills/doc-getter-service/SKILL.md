---
name: doc-getter-service
description: Expose and extend the doc_getter crawler as a FastAPI job service with async crawl submission, status polling, cancellation, manifest/archive downloads, and per-file retrieval. Use when asked to wrap the crawler as an API, add service endpoints, design request/response models, or package the workflow as an installable Codex skill.
---

# Doc Getter Service

Use this skill when the task is about turning the crawler into a service rather than a local-only script.

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
- `GET /v1/crawls/{job_id}/archive` to download a zip of generated Markdown
- `GET /v1/crawls/{job_id}/files` to list generated files
- `GET /v1/crawls/{job_id}/files/{path}` to fetch one generated file

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
