---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/createguardrailresponse"
title: "CreateGuardrailResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:04.305776+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

CreateGuardrailResponse - TypeScript SDK

CreateGuardrailResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateGuardrailResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: CreateGuardrailResponse = { |
| 4 | data: { |
| 5 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 6 | name: "My New Guardrail", |
| 7 | createdAt: "2025-08-24T10:30:00Z", |
| 8 | }, |
| 9 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [models.Guardrail](../guardrail/index.md) | ✔️ | N/A | `{"id": "550e8400-e29b-41d4-a716-446655440000","name": "Production Guardrail","description": "Guardrail for production environment","limit_usd": 100,"reset_interval": "monthly","allowed_providers": ["openai","anthropic","google"],"ignored_providers": null,"allowed_models": null,"enforce_zdr": false,"created_at": "2025-08-24T10:30:00Z","updated_at": "2025-08-24T15:45:00Z"}` |
