---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/data"
title: "Data Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.741364+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

Data - TypeScript SDK

Data type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Model count data

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Data } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: Data = { |
| 4 | count: 150, |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `count` | *number* | ✔️ | Total number of available models | 150 |
