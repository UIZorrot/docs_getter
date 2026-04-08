---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/modellinks"
title: "ModelLinks Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:18.654439+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ModelLinks - TypeScript SDK

ModelLinks type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Related API endpoints and resources for this model.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ModelLinks } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ModelLinks = { |
| 4 | details: "/api/v1/models/openai/gpt-5.4/endpoints", |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `details` | *string* | ✔️ | URL for the model details/endpoints API | /api/v1/models/openai/gpt-5.4/endpoints |
