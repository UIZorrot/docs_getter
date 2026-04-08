---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/bulk-unassign-members-from-guardrail"
title: "Bulk unassign members from a guardrail | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:26.833706+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](../list-guardrails/index.md)

# Bulk unassign members from a guardrail

POST

https://openrouter.ai/api/v1/guardrails/:id/assignments/members/remove

POST

/api/v1/guardrails/:id/assignments/members/remove

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/members/remove \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "member_user_ids": [ |
| 6 | "user_abc123", |
| 7 | "user_def456" |
| 8 | ] |
| 9 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "unassigned_count": 2 |
| 3 | } |
```

Unassign multiple organization members from a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

idstringRequired`format: "uuid"`

The unique identifier of the guardrail

### Request

This endpoint expects an object.

member\_user\_idslist of stringsRequired

Array of member user IDs to unassign from the guardrail

### Response

Unassignment result

unassigned\_countinteger

Number of members successfully unassigned

### Errors

400

Bad Request Error

401

Unauthorized Error

404

Not Found Error

500

Internal Server Error
