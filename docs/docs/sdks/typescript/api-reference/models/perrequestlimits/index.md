---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/perrequestlimits"
title: "PerRequestLimits Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:18.609033+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

PerRequestLimits - TypeScript SDK

PerRequestLimits type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Per-request token limits

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { PerRequestLimits } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: PerRequestLimits = { |
| 4 | promptTokens: 1000, |
| 5 | completionTokens: 1000, |
| 6 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `promptTokens` | *number* | ✔️ | Maximum prompt tokens per request | 1000 |
| `completionTokens` | *number* | ✔️ | Maximum completion tokens per request | 1000 |
