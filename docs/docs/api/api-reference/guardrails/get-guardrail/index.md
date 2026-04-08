---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/get-guardrail"
title: "Get a guardrail | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.272887+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](../list-guardrails/index.md)

# Get a guardrail

GET

https://openrouter.ai/api/v1/guardrails/:id

GET

/api/v1/guardrails/:id

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000 \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "created_at": "2025-08-24T10:30:00Z", |
| 4 | "id": "550e8400-e29b-41d4-a716-446655440000", |
| 5 | "name": "Production Guardrail", |
| 6 | "allowed_providers": [ |
| 7 | "openai", |
| 8 | "anthropic", |
| 9 | "google" |
| 10 | ], |
| 11 | "description": "Guardrail for production environment", |
| 12 | "enforce_zdr": false, |
| 13 | "limit_usd": 100, |
| 14 | "reset_interval": "monthly", |
| 15 | "updated_at": "2025-08-24T15:45:00Z" |
| 16 | } |
| 17 | } |
```

Get a single guardrail by ID. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

idstringRequired`format: "uuid"`

The unique identifier of the guardrail to retrieve

### Response

Guardrail details

dataobject

### Errors

401

Unauthorized Error

404

Not Found Error

500

Internal Server Error
