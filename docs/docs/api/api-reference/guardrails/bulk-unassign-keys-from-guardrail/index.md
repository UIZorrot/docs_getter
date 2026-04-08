---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/bulk-unassign-keys-from-guardrail"
title: "Bulk unassign keys from a guardrail | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:26.389293+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](../list-guardrails/index.md)

# Bulk unassign keys from a guardrail

POST

https://openrouter.ai/api/v1/guardrails/:id/assignments/keys/remove

POST

/api/v1/guardrails/:id/assignments/keys/remove

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys/remove \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "key_hashes": [ |
| 6 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93" |
| 7 | ] |
| 8 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "unassigned_count": 3 |
| 3 | } |
```

Unassign multiple API keys from a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

idstringRequired`format: "uuid"`

The unique identifier of the guardrail

### Request

This endpoint expects an object.

key\_hasheslist of stringsRequired

Array of API key hashes to unassign from the guardrail

### Response

Unassignment result

unassigned\_countinteger

Number of keys successfully unassigned

### Errors

400

Bad Request Error

401

Unauthorized Error

404

Not Found Error

500

Internal Server Error
