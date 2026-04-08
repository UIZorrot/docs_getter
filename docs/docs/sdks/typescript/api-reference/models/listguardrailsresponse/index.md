---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/listguardrailsresponse"
title: "ListGuardrailsResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.193946+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ListGuardrailsResponse - TypeScript SDK

ListGuardrailsResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListGuardrailsResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ListGuardrailsResponse = { |
| 4 | data: [ |
| 5 | { |
| 6 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 7 | name: "Production Guardrail", |
| 8 | createdAt: "2025-08-24T10:30:00Z", |
| 9 | }, |
| 10 | ], |
| 11 | totalCount: 1, |
| 12 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [models.Guardrail](../guardrail/index.md)[] | ✔️ | List of guardrails |  |
| `totalCount` | *number* | ✔️ | Total number of guardrails | 25 |
