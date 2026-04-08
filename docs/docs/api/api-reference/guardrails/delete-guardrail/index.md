---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/delete-guardrail"
title: "Delete a guardrail | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.032284+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](../list-guardrails/index.md)

# Delete a guardrail

DELETE

https://openrouter.ai/api/v1/guardrails/:id

DELETE

/api/v1/guardrails/:id

```
|  |  |
| --- | --- |
| 1 | curl -X DELETE https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000 \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "deleted": true |
| 3 | } |
```

Delete an existing guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

idstringRequired`format: "uuid"`

The unique identifier of the guardrail to delete

### Response

Guardrail deleted successfully

deletedtrue

Confirmation that the guardrail was deleted

### Errors

401

Unauthorized Error

404

Not Found Error

500

Internal Server Error
