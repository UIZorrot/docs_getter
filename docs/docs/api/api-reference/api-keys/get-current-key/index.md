---
source_url: "https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key"
title: "Get current API key | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:24.883268+00:00"
---
[API Reference](../../responses/create-responses/index.md)[API Keys](../list/index.md)

# Get current API key

GET

https://openrouter.ai/api/v1/key

GET

/api/v1/key

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/key \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "label": "sk-or-v1-au7...890", |
| 4 | "limit": 100, |
| 5 | "usage": 25.5, |
| 6 | "usage_daily": 25.5, |
| 7 | "usage_weekly": 25.5, |
| 8 | "usage_monthly": 25.5, |
| 9 | "byok_usage": 17.38, |
| 10 | "byok_usage_daily": 17.38, |
| 11 | "byok_usage_weekly": 17.38, |
| 12 | "byok_usage_monthly": 17.38, |
| 13 | "is_free_tier": false, |
| 14 | "is_management_key": false, |
| 15 | "limit_remaining": 74.5, |
| 16 | "limit_reset": "monthly", |
| 17 | "include_byok_in_limit": false, |
| 18 | "creator_user_id": "user_2dHFtVWx2n56w6HkM0000000000", |
| 19 | "is_provisioning_key": false, |
| 20 | "rate_limit": { |
| 21 | "requests": 1000, |
| 22 | "interval": "1h", |
| 23 | "note": "This field is deprecated and safe to ignore." |
| 24 | }, |
| 25 | "expires_at": "2027-12-31T23:59:59Z" |
| 26 | } |
| 27 | } |
```

Get information on the API key associated with the current authentication session

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Response

API key details

dataobject

Current API key information

### Errors

401

Unauthorized Error

500

Internal Server Error
