# doc_getter

Mirror documentation sites into Markdown, either as a local CLI run or as a FastAPI job service.

## What it does

- Crawls docs sites from a seed URL
- Discovers pages from robots.txt and sitemap.xml
- Rewrites internal links to local Markdown paths
- Writes a manifest with crawl metadata
- Supports a service mode with job polling, cancellation, archives, and file download

## Installation

```bash
uv sync
```

## CLI usage

```bash
uv run python main.py https://openrouter.ai/docs/ --output ./docs --workers 10
```

Useful flags:

- `--scope-prefix /docs/`
- `--max-pages 200`
- `--max-depth 10`
- `--timeout 30`
- `--delay 0.5`
- `--no-sitemaps`
- `--verbose`

## Service mode

Run the API server:

```bash
uv run python service.py
```

or:

```bash
uv run uvicorn service:app --host 0.0.0.0 --port 8000
```

The service stores each crawl under `runs/<job_id>/` by default.

### Create a crawl job

```bash
curl -X POST http://127.0.0.1:8000/v1/crawls \
  -H 'Content-Type: application/json' \
  -d '{
    "start_url": "https://openrouter.ai/docs/",
    "scope_prefix": "/docs/",
    "workers": 10
  }'
```

### Poll the job

```bash
curl http://127.0.0.1:8000/v1/crawls/<job_id>
```

### Download outputs

- Manifest: `GET /v1/crawls/<job_id>/manifest`
- Zip archive: `GET /v1/crawls/<job_id>/archive`
- File list: `GET /v1/crawls/<job_id>/files`
- One file: `GET /v1/crawls/<job_id>/files/<path>`
- Cancel job: `POST /v1/crawls/<job_id>/cancel`

## Skill package

A reusable Codex skill is included at:

- `skills/doc-getter-service/SKILL.md`

To install it, copy that folder into your Codex skills directory, for example:

```bash
~/.codex/skills/doc-getter-service
```

or on Windows:

```powershell
$env:USERPROFILE\.codex\skills\doc-getter-service
```

## Output structure

Each crawl still writes Markdown files and `_mirror-manifest.json` to disk, so the service and CLI share the same crawl engine and artifact format.
