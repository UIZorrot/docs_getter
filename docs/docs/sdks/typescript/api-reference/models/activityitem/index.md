---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/activityitem"
title: "ActivityItem Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:14.512722+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ActivityItem - TypeScript SDK

ActivityItem type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ActivityItem } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ActivityItem = { |
| 4 | date: "2025-08-24", |
| 5 | model: "openai/gpt-4.1", |
| 6 | modelPermaslug: "openai/gpt-4.1-2025-04-14", |
| 7 | endpointId: "550e8400-e29b-41d4-a716-446655440000", |
| 8 | providerName: "OpenAI", |
| 9 | usage: 0.015, |
| 10 | byokUsageInference: 0.012, |
| 11 | requests: 5, |
| 12 | promptTokens: 50, |
| 13 | completionTokens: 125, |
| 14 | reasoningTokens: 25, |
| 15 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `date` | *string* | ✔️ | Date of the activity (YYYY-MM-DD format) | 2025-08-24 |
| `model` | *string* | ✔️ | Model slug (e.g., “openai/gpt-4.1”) | openai/gpt-4.1 |
| `modelPermaslug` | *string* | ✔️ | Model permaslug (e.g., “openai/gpt-4.1-2025-04-14”) | openai/gpt-4.1-2025-04-14 |
| `endpointId` | *string* | ✔️ | Unique identifier for the endpoint | 550e8400-e29b-41d4-a716-446655440000 |
| `providerName` | *string* | ✔️ | Name of the provider serving this endpoint | OpenAI |
| `usage` | *number* | ✔️ | Total cost in USD (OpenRouter credits spent) | 0.015 |
| `byokUsageInference` | *number* | ✔️ | BYOK inference cost in USD (external credits spent) | 0.012 |
| `requests` | *number* | ✔️ | Number of requests made | 5 |
| `promptTokens` | *number* | ✔️ | Total prompt tokens used | 50 |
| `completionTokens` | *number* | ✔️ | Total completion tokens generated | 125 |
| `reasoningTokens` | *number* | ✔️ | Total reasoning tokens used | 25 |
