---
source_url: "https://openrouter.ai/docs/api/api-reference/api-keys/create-keys"
title: "Create a new API key | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:56.361723+00:00"
---
[API Reference](../../responses/create-responses/index.md)[API Keys](../list/index.md)

# Create a new API key

POST

https://openrouter.ai/api/v1/keys

POST

/api/v1/keys

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/keys \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "name": "Analytics Service Key", |
| 6 | "limit": 150, |
| 7 | "limit_reset": "monthly", |
| 8 | "include_byok_in_limit": true, |
| 9 | "expires_at": "2028-06-30T23:59:59Z" |
| 10 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "hash": "a3f5b7c9d8e1f23456789abcdeffedcba9876543210fedcba1234567890abcdef", |
| 4 | "name": "Analytics Service Key", |
| 5 | "label": "sk-or-v1-analytics-1a2b3c4d5e6f", |
| 6 | "disabled": false, |
| 7 | "limit": 150, |
| 8 | "limit_remaining": 150, |
| 9 | "limit_reset": "monthly", |
| 10 | "include_byok_in_limit": true, |
| 11 | "usage": 0, |
| 12 | "usage_daily": 0, |
| 13 | "usage_weekly": 0, |
| 14 | "usage_monthly": 0, |
| 15 | "byok_usage": 0, |
| 16 | "byok_usage_daily": 0, |
| 17 | "byok_usage_weekly": 0, |
| 18 | "byok_usage_monthly": 0, |
| 19 | "created_at": "2024-06-01T09:00:00Z", |
| 20 | "creator_user_id": "user_7fGhtYx9kLmN1234567890000", |
| 21 | "expires_at": "2028-06-30T23:59:59Z" |
| 22 | }, |
| 23 | "key": "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" |
| 24 | } |
```

Create a new API key for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

namestringRequired`>=1 character`

Name for the new API key

limitdoubleOptional

Optional spending limit for the API key in USD

limit\_resetenum or nullOptional

Type of limit reset for the API key (daily, weekly, monthly, or null for no reset). Resets happen automatically at midnight UTC, and weeks are Monday through Sunday.

Allowed values:

include\_byok\_in\_limitbooleanOptional

Whether to include BYOK usage in the limit

expires\_atdatetime or nullOptional

Optional ISO 8601 UTC timestamp when the API key should expire. Must be UTC, other timezones will be rejected

creator\_user\_idstring or nullOptional`>=1 character`

Optional user ID of the key creator. Only meaningful for organization-owned keys where a specific member is creating the key.

### Response

API key created successfully

dataobject

The created API key information

keystring

The actual API key string (only shown once)

### Errors

400

Bad Request Error

401

Unauthorized Error

429

Too Many Requests Error

500

Internal Server Error
