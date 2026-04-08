---
source_url: "https://openrouter.ai/docs/api/api-reference/api-keys/update-keys"
title: "Update an API key | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:25.549194+00:00"
---
[API Reference](../../responses/create-responses/index.md)[API Keys](../list/index.md)

# Update an API key

PATCH

https://openrouter.ai/api/v1/keys/:hash

PATCH

/api/v1/keys/:hash

```
|  |  |
| --- | --- |
| 1 | curl -X PATCH https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943 \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "name": "Updated API Key Name", |
| 6 | "disabled": false, |
| 7 | "limit": 75, |
| 8 | "limit_reset": "daily", |
| 9 | "include_byok_in_limit": true |
| 10 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "hash": "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943", |
| 4 | "name": "Updated API Key Name", |
| 5 | "label": "Updated API Key Name", |
| 6 | "disabled": false, |
| 7 | "limit": 75, |
| 8 | "limit_remaining": 49.5, |
| 9 | "limit_reset": "daily", |
| 10 | "include_byok_in_limit": true, |
| 11 | "usage": 25.5, |
| 12 | "usage_daily": 25.5, |
| 13 | "usage_weekly": 25.5, |
| 14 | "usage_monthly": 25.5, |
| 15 | "byok_usage": 17.38, |
| 16 | "byok_usage_daily": 17.38, |
| 17 | "byok_usage_weekly": 17.38, |
| 18 | "byok_usage_monthly": 17.38, |
| 19 | "created_at": "2025-08-24T10:30:00Z", |
| 20 | "updated_at": "2025-08-24T16:00:00Z", |
| 21 | "creator_user_id": "user_2dHFtVWx2n56w6HkM0000000000" |
| 22 | } |
| 23 | } |
```

Update an existing API key. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

hashstringRequired

The hash identifier of the API key to update

### Request

This endpoint expects an object.

namestringOptional

New name for the API key

disabledbooleanOptional

Whether to disable the API key

limitdoubleOptional

New spending limit for the API key in USD

limit\_resetenum or nullOptional

New limit reset type for the API key (daily, weekly, monthly, or null for no reset). Resets happen automatically at midnight UTC, and weeks are Monday through Sunday.

Allowed values:

include\_byok\_in\_limitbooleanOptional

Whether to include BYOK usage in the limit

### Response

API key updated successfully

dataobject

The updated API key information

### Errors

400

Bad Request Error

401

Unauthorized Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error
