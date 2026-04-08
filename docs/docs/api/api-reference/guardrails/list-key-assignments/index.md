---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/list-key-assignments"
title: "List all key assignments | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.336443+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](../list-guardrails/index.md)

# List all key assignments

GET

https://openrouter.ai/api/v1/guardrails/assignments/keys

GET

/api/v1/guardrails/assignments/keys

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/guardrails/assignments/keys \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "id": "550e8400-e29b-41d4-a716-446655440000", |
| 5 | "key_hash": "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 6 | "guardrail_id": "550e8400-e29b-41d4-a716-446655440001", |
| 7 | "key_name": "Production Key", |
| 8 | "key_label": "prod-key", |
| 9 | "assigned_by": "user_abc123", |
| 10 | "created_at": "2025-08-24T10:30:00Z" |
| 11 | } |
| 12 | ], |
| 13 | "total_count": 1 |
| 14 | } |
```

List all API key guardrail assignments for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

offsetintegerOptional`>=0`

Number of records to skip for pagination

limitintegerOptional`1-100`

Maximum number of records to return (max 100)

### Response

List of key assignments

datalist of objects

List of key assignments

total\_countinteger

Total number of key assignments for this guardrail

### Errors

401

Unauthorized Error

500

Internal Server Error
