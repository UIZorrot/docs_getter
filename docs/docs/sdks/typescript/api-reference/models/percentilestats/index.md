---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/percentilestats"
title: "PercentileStats Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:18.259646+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

PercentileStats - TypeScript SDK

PercentileStats type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Latency percentiles in milliseconds over the last 30 minutes. Latency measures time to first token. Only visible when authenticated with an API key or cookie; returns null for unauthenticated requests.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { PercentileStats } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: PercentileStats = { |
| 4 | p50: 25.5, |
| 5 | p75: 35.2, |
| 6 | p90: 48.7, |
| 7 | p99: 85.3, |
| 8 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `p50` | *number* | ✔️ | Median (50th percentile) | 25.5 |
| `p75` | *number* | ✔️ | 75th percentile | 35.2 |
| `p90` | *number* | ✔️ | 90th percentile | 48.7 |
| `p99` | *number* | ✔️ | 99th percentile | 85.3 |
