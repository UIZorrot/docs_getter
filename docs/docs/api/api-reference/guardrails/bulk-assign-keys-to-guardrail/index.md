---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/bulk-assign-keys-to-guardrail"
title: "Bulk assign keys to a guardrail | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:26.181112+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](../list-guardrails/index.md)

# Bulk assign keys to a guardrail

POST

https://openrouter.ai/api/v1/guardrails/:id/assignments/keys

POST

/api/v1/guardrails/:id/assignments/keys

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000/assignments/keys \ |
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
| 2 | "assigned_count": 3 |
| 3 | } |
```

Assign multiple API keys to a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

idstringRequired`format: "uuid"`

The unique identifier of the guardrail

### Request

This endpoint expects an object.

key\_hasheslist of stringsRequired

Array of API key hashes to assign to the guardrail

### Response

Assignment result

assigned\_countinteger

Number of keys successfully assigned

### Errors

400

Bad Request Error

401

Unauthorized Error

404

Not Found Error

500

Internal Server Error
