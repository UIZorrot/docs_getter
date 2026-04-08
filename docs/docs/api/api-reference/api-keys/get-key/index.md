---
source_url: "https://openrouter.ai/docs/api/api-reference/api-keys/get-key"
title: "Get a single API key | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:24.966433+00:00"
---
[API Reference](../../responses/create-responses/index.md)[API Keys](../list/index.md)

# Get a single API key

GET

https://openrouter.ai/api/v1/keys/:hash

GET

/api/v1/keys/:hash

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/keys/f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943 \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "hash": "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943", |
| 4 | "name": "My Production Key", |
| 5 | "label": "Production API Key", |
| 6 | "disabled": false, |
| 7 | "limit": 100, |
| 8 | "limit_remaining": 74.5, |
| 9 | "limit_reset": "monthly", |
| 10 | "include_byok_in_limit": false, |
| 11 | "usage": 25.5, |
| 12 | "usage_daily": 25.5, |
| 13 | "usage_weekly": 25.5, |
| 14 | "usage_monthly": 25.5, |
| 15 | "byok_usage": 17.38, |
| 16 | "byok_usage_daily": 17.38, |
| 17 | "byok_usage_weekly": 17.38, |
| 18 | "byok_usage_monthly": 17.38, |
| 19 | "created_at": "2025-08-24T10:30:00Z", |
| 20 | "updated_at": "2025-08-24T15:45:00Z", |
| 21 | "creator_user_id": "user_2dHFtVWx2n56w6HkM0000000000", |
| 22 | "expires_at": "2027-12-31T23:59:59Z" |
| 23 | } |
| 24 | } |
```

Get a single API key by hash. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

hashstringRequired

The hash identifier of the API key to retrieve

### Response

API key details

dataobject

The API key information

### Errors

401

Unauthorized Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error
