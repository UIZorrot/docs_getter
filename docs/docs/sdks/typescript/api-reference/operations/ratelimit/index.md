---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/ratelimit"
title: "RateLimit Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.929852+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

~~RateLimit~~ - TypeScript SDK

~~RateLimit~~ type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Legacy rate limit information about a key. Will always return -1.

> ⚠️ **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { RateLimit } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: RateLimit = { |
| 4 | requests: 1000, |
| 5 | interval: "1h", |
| 6 | note: "This field is deprecated and safe to ignore.", |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `requests` | *number* | ✔️ | Number of requests allowed per interval | 1000 |
| `interval` | *string* | ✔️ | Rate limit interval | 1h |
| `note` | *string* | ✔️ | Note about the rate limit | This field is deprecated and safe to ignore. |
