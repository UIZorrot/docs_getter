---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/list-guardrails"
title: "List guardrails | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.188506+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](index.md)

# List guardrails

GET

https://openrouter.ai/api/v1/guardrails

GET

/api/v1/guardrails

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/guardrails \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "id": "550e8400-e29b-41d4-a716-446655440000", |
| 5 | "name": "Production Guardrail", |
| 6 | "created_at": "2025-08-24T10:30:00Z", |
| 7 | "description": "Guardrail for production environment", |
| 8 | "limit_usd": 100, |
| 9 | "reset_interval": "monthly", |
| 10 | "allowed_providers": [ |
| 11 | "openai", |
| 12 | "anthropic", |
| 13 | "google" |
| 14 | ], |
| 15 | "enforce_zdr": false, |
| 16 | "updated_at": "2025-08-24T15:45:00Z" |
| 17 | } |
| 18 | ], |
| 19 | "total_count": 1 |
| 20 | } |
```

List all guardrails for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

offsetintegerOptional`>=0`

Number of records to skip for pagination

limitintegerOptional`1-100`

Maximum number of records to return (max 100)

### Response

List of guardrails

datalist of objects

List of guardrails

total\_countinteger

Total number of guardrails

### Errors

401

Unauthorized Error

500

Internal Server Error
