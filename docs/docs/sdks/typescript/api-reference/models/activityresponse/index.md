---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/activityresponse"
title: "ActivityResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:03.470383+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ActivityResponse - TypeScript SDK

ActivityResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ActivityResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ActivityResponse = { |
| 4 | data: [ |
| 5 | { |
| 6 | date: "2025-08-24", |
| 7 | model: "openai/gpt-4.1", |
| 8 | modelPermaslug: "openai/gpt-4.1-2025-04-14", |
| 9 | endpointId: "550e8400-e29b-41d4-a716-446655440000", |
| 10 | providerName: "OpenAI", |
| 11 | usage: 0.015, |
| 12 | byokUsageInference: 0.012, |
| 13 | requests: 5, |
| 14 | promptTokens: 50, |
| 15 | completionTokens: 125, |
| 16 | reasoningTokens: 25, |
| 17 | }, |
| 18 | ], |
| 19 | }; |
```

## Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | [models.ActivityItem](../activityitem/index.md)[] | ✔️ | List of activity items |
