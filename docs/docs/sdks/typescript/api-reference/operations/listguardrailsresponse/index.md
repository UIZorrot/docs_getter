---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listguardrailsresponse"
title: "ListGuardrailsResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:04.218531+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

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
| 1 | import { ListGuardrailsResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListGuardrailsResponse = { |
| 4 | result: { |
| 5 | data: [ |
| 6 | { |
| 7 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 8 | name: "Production Guardrail", |
| 9 | createdAt: "2025-08-24T10:30:00Z", |
| 10 | }, |
| 11 | ], |
| 12 | totalCount: 1, |
| 13 | }, |
| 14 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `result` | [models.ListGuardrailsResponse](../../models/listguardrailsresponse/index.md) | ✔️ | N/A | `{"data": [{"id": "550e8400-e29b-41d4-a716-446655440000","name": "Production Guardrail","description": "Guardrail for production environment","limit_usd": 100,"reset_interval": "monthly","allowed_providers": ["openai","anthropic","google"],"ignored_providers": null,"allowed_models": null,"enforce_zdr": false,"created_at": "2025-08-24T10:30:00Z","updated_at": "2025-08-24T15:45:00Z"}` ], “total\_count”: `1<br />`} |
