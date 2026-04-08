---
source_url: "https://openrouter.ai/docs/api/api-reference/api-keys/list"
title: "List API keys | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:25.629874+00:00"
---
[API Reference](../../responses/create-responses/index.md)[API Keys](index.md)

# List API keys

GET

https://openrouter.ai/api/v1/keys

GET

/api/v1/keys

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/keys \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "hash": "f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943", |
| 5 | "name": "My Production Key", |
| 6 | "label": "Production API Key", |
| 7 | "disabled": false, |
| 8 | "limit": 100, |
| 9 | "limit_remaining": 74.5, |
| 10 | "limit_reset": "monthly", |
| 11 | "include_byok_in_limit": false, |
| 12 | "usage": 25.5, |
| 13 | "usage_daily": 25.5, |
| 14 | "usage_weekly": 25.5, |
| 15 | "usage_monthly": 25.5, |
| 16 | "byok_usage": 17.38, |
| 17 | "byok_usage_daily": 17.38, |
| 18 | "byok_usage_weekly": 17.38, |
| 19 | "byok_usage_monthly": 17.38, |
| 20 | "created_at": "2025-08-24T10:30:00Z", |
| 21 | "updated_at": "2025-08-24T15:45:00Z", |
| 22 | "creator_user_id": "user_2dHFtVWx2n56w6HkM0000000000", |
| 23 | "expires_at": "2027-12-31T23:59:59Z" |
| 24 | } |
| 25 | ] |
| 26 | } |
```

List all API keys for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

include\_disabledstringOptional

Whether to include disabled API keys in the response

offsetintegerOptional`>=0`

Number of API keys to skip for pagination

### Response

List of API keys

datalist of objects

List of API keys

### Errors

401

Unauthorized Error

429

Too Many Requests Error

500

Internal Server Error
