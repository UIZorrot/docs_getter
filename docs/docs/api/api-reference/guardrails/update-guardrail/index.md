---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/update-guardrail"
title: "Update a guardrail | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.488897+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](../list-guardrails/index.md)

# Update a guardrail

PATCH

https://openrouter.ai/api/v1/guardrails/:id

PATCH

/api/v1/guardrails/:id

```
|  |  |
| --- | --- |
| 1 | curl -X PATCH https://openrouter.ai/api/v1/guardrails/550e8400-e29b-41d4-a716-446655440000 \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "name": "Updated Guardrail Name", |
| 6 | "description": "Updated description", |
| 7 | "limit_usd": 75, |
| 8 | "reset_interval": "weekly" |
| 9 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "created_at": "2025-08-24T10:30:00Z", |
| 4 | "id": "550e8400-e29b-41d4-a716-446655440000", |
| 5 | "name": "Updated Guardrail Name", |
| 6 | "allowed_providers": [ |
| 7 | "openai" |
| 8 | ], |
| 9 | "description": "Updated description", |
| 10 | "enforce_zdr": true, |
| 11 | "limit_usd": 75, |
| 12 | "reset_interval": "weekly", |
| 13 | "updated_at": "2025-08-24T16:00:00Z" |
| 14 | } |
| 15 | } |
```

Update an existing guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

idstringRequired`format: "uuid"`

The unique identifier of the guardrail to update

### Request

This endpoint expects an object.

namestringOptional`1-200 characters`

New name for the guardrail

descriptionstring or nullOptional`<=1000 characters`

New description for the guardrail

limit\_usddoubleOptional

New spending limit in USD

reset\_intervalenumOptional

Interval at which the limit resets (daily, weekly, monthly)

Allowed values:

allowed\_providerslist of strings or nullOptional

New list of allowed provider IDs

ignored\_providerslist of strings or nullOptional

List of provider IDs to exclude from routing

allowed\_modelslist of strings or nullOptional

Array of model identifiers (slug or canonical\_slug accepted)

enforce\_zdrboolean or nullOptional

Whether to enforce zero data retention

### Response

Guardrail updated successfully

dataobject

### Errors

400

Bad Request Error

401

Unauthorized Error

404

Not Found Error

500

Internal Server Error
