# doc_getter

A standalone tool for crawling and mirroring documentation websites into local Markdown files. Perfect for creating offline, searchable copies of API docs and technical documentation.

## Features

- **Smart crawling**: Automatically discovers pages via sitemaps and robots.txt
- **Scope control**: Limits crawling to specific URL prefixes (e.g., `/docs/`)
- **Markdown conversion**: Converts HTML to clean Markdown with front matter metadata
- **Link rewriting**: Internal links point to local files; external links remain unchanged
- **Live logging**: Real-time progress with detailed debug information
- **Manifest tracking**: JSON metadata of all crawled pages and errors
- **Configurable**: Control depth, page limits, timeouts, and user-agent

## Installation

Requires Python 3.12+

```bash
cd doc_getter
uv sync
```

## Quick Start

```bash
uv run python main.py https://openrouter.ai/docs/ --output ../docs
```

This will:
1. Discover seed URLs from the sitemap / robots.txt
2. Crawl all pages within the `/docs/` scope (up to 500 by default)
3. Fetch pages concurrently (5 workers by default)
4. Save Markdown files to `../docs/`
5. Generate a `_mirror-manifest.json` with crawl metadata

## Options

### URL & Scope
- `--scope-prefix /docs/` — Limit crawling to paths under this prefix (auto-detected by default)
- `--no-sitemaps` — Skip robots.txt and sitemap.xml discovery, crawl only from links

### Crawl Control
- `--max-pages 200` — Stop after crawling N pages (default: 500)
- `--max-depth 10` — Follow links up to N levels deep (default: 20)
- `--workers 10` — Number of concurrent page fetches (default: 5)
- `--timeout 30` — Request timeout per page in seconds (default: 30)
- `--delay 0.5` — Wait N seconds between each batch of fetches (default: 0)

### Other
- `--user-agent "Custom string"` — Override the User-Agent header
- `--verbose` — Enable debug logging to see every queued URL and redirect

## Logging

By default, you'll see INFO-level progress as pages are written:

```
2026-04-08 10:30:15 - INFO - Starting crawl: https://openrouter.ai/docs/
2026-04-08 10:30:15 - INFO - Max pages: 500, Max depth: 20, Workers: 5
2026-04-08 10:30:15 - INFO - Discovered 150 URLs from sitemaps
2026-04-08 10:30:16 - INFO - [1/500] https://openrouter.ai/docs/ (queue=149, in-flight=4)
2026-04-08 10:30:16 - INFO - [2/500] https://openrouter.ai/docs/api/ (queue=155, in-flight=4)
...
```

Add `--verbose` to see every redirect and queued URL:

```bash
uv run python main.py https://example.com/docs --output ../docs --verbose
```

## Output Structure

```
docs/
├── example.com/
│   ├── index.md                 # Homepage
│   ├── api/
│   │   ├── index.md            # /api/ page
│   │   └── endpoints/
│   │       └── index.md        # /api/endpoints/ page
│   └── _mirror-manifest.json   # Crawl metadata
```

Each Markdown file includes front matter:

```yaml
---
source_url: https://example.com/docs/api
title: API Reference
crawled_at: 2026-04-08T10:30:17+00:00
---

# API Reference
...
```

## Manifest

The `_mirror-manifest.json` contains crawl statistics:

```json
{
  "start_url": "https://openrouter.ai/docs/",
  "page_count": 145,
  "skipped_count": 3,
  "started_at": "2026-04-08T10:30:15.123456+00:00",
  "finished_at": "2026-04-08T10:35:42.654321+00:00",
  "pages": [
    {
      "source_url": "https://openrouter.ai/docs/",
      "final_url": "https://openrouter.ai/docs/",
      "title": "OpenRouter Docs",
      "output_path": "index.md",
      "discovered_links": 24,
      "queued_links": 18,
      "status_code": 200
    }
  ],
  "skipped": [
    {
      "url": "https://openrouter.ai/docs/pdf/guide.pdf",
      "error": "Skipped non-HTML response (application/pdf)"
    }
  ]
}
```

## Examples

**Crawl with depth limit:**
```bash
uv run python main.py https://api.example.com/docs --max-depth 5 --output ./docs
```

**Crawl slowly to be respectful:**
```bash
uv run python main.py https://docs.example.com --delay 1.0 --output ./docs
```

**Crawl a specific subdirectory:**
```bash
uv run python main.py https://docs.example.com/python/ --scope-prefix /python/ --output ./docs
```

**Crawl without sitemaps (links only):**
```bash
uv run python main.py https://docs.example.com --no-sitemaps --output ./docs
```
