---
source_url: "https://openrouter.ai/docs/guides/administration/crypto-api"
title: "Crypto API | Deprecated Coinbase Commerce Endpoint | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:31.463136+00:00"
---
[Guides](../activity-export/index.md)[Administration](../activity-export/index.md)

# Crypto API

Coinbase Commerce API deprecation

##### 

Coinbase deprecated the APIs used by this flow, so `POST /api/v1/credits/coinbase` has been
removed and now returns `410 Gone`.

## Status

The old programmatic Coinbase Commerce charge flow is no longer supported because Coinbase
deprecated the underlying APIs it relied on. This includes the legacy flow that returned on-chain
calldata for direct settlement.

## What To Use Instead

Use the web credits purchase flow on your
[credits page](https://openrouter.ai/settings/credits). OpenRouter now uses Coinbase Business
Checkouts for active Coinbase credit purchases.

## Affected Endpoint

```
|  |
| --- |
| POST /api/v1/credits/coinbase |
```

Current behavior:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "error": { |
| 3 | "code": 410, |
| 4 | "message": "The Coinbase APIs used by this endpoint have been deprecated, so the Coinbase Commerce credits API has been removed. Use the web credits purchase flow instead." |
| 5 | } |
| 6 | } |
```

## Notes

- Existing SDK surfaces may still contain the deprecated `createCoinbaseCharge` method until the
  next SDK regeneration.
- New Coinbase webhook handling is for Coinbase Business Checkouts only.
- Legacy Coinbase Commerce environment variables are no longer used.
