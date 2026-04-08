---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/list-member-assignments"
title: "List all member assignments | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.404994+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](../list-guardrails/index.md)

# List all member assignments

GET

https://openrouter.ai/api/v1/guardrails/assignments/members

GET

/api/v1/guardrails/assignments/members

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/guardrails/assignments/members \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "id": "550e8400-e29b-41d4-a716-446655440000", |
| 5 | "user_id": "user_abc123", |
| 6 | "organization_id": "org_xyz789", |
| 7 | "guardrail_id": "550e8400-e29b-41d4-a716-446655440001", |
| 8 | "assigned_by": "user_abc123", |
| 9 | "created_at": "2025-08-24T10:30:00Z" |
| 10 | } |
| 11 | ], |
| 12 | "total_count": 1 |
| 13 | } |
```

List all organization member guardrail assignments for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

offsetintegerOptional`>=0`

Number of records to skip for pagination

limitintegerOptional`1-100`

Maximum number of records to return (max 100)

### Response

List of member assignments

datalist of objects

List of member assignments

total\_countinteger

Total number of member assignments

### Errors

401

Unauthorized Error

500

Internal Server Error
