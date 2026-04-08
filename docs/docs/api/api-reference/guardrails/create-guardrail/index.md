---
source_url: "https://openrouter.ai/docs/api/api-reference/guardrails/create-guardrail"
title: "Create a guardrail | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:26.770850+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Guardrails](../list-guardrails/index.md)

# Create a guardrail

POST

https://openrouter.ai/api/v1/guardrails

POST

/api/v1/guardrails

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/guardrails \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "name": "My New Guardrail", |
| 6 | "description": "A guardrail for limiting API usage", |
| 7 | "limit_usd": 50, |
| 8 | "reset_interval": "monthly", |
| 9 | "allowed_providers": [ |
| 10 | "openai", |
| 11 | "anthropic", |
| 12 | "deepseek" |
| 13 | ], |
| 14 | "enforce_zdr": false |
| 15 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "created_at": "2025-08-24T10:30:00Z", |
| 4 | "id": "550e8400-e29b-41d4-a716-446655440000", |
| 5 | "name": "My New Guardrail", |
| 6 | "allowed_providers": [ |
| 7 | "openai", |
| 8 | "anthropic", |
| 9 | "google" |
| 10 | ], |
| 11 | "description": "A guardrail for limiting API usage", |
| 12 | "enforce_zdr": false, |
| 13 | "limit_usd": 50, |
| 14 | "reset_interval": "monthly" |
| 15 | } |
| 16 | } |
```

Create a new guardrail for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

namestringRequired`1-200 characters`

Name for the new guardrail

descriptionstring or nullOptional`<=1000 characters`

Description of the guardrail

limit\_usddoubleOptional

Spending limit in USD

reset\_intervalenumOptional

Interval at which the limit resets (daily, weekly, monthly)

Allowed values:

allowed\_providerslist of strings or nullOptional

List of allowed provider IDs

ignored\_providerslist of strings or nullOptional

List of provider IDs to exclude from routing

allowed\_modelslist of strings or nullOptional

Array of model identifiers (slug or canonical\_slug accepted)

enforce\_zdrboolean or nullOptional

Whether to enforce zero data retention

### Response

Guardrail created successfully

dataobject

### Errors

400

Bad Request Error

401

Unauthorized Error

500

Internal Server Error
