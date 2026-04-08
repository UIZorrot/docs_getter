---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/modelscountresponse"
title: "ModelsCountResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:05.856031+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ModelsCountResponse - TypeScript SDK

ModelsCountResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Model count data

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ModelsCountResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ModelsCountResponse = { |
| 4 | data: { |
| 5 | count: 150, |
| 6 | }, |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [models.Data](../data/index.md) | ✔️ | Model count data | `{"count": 150}` |
