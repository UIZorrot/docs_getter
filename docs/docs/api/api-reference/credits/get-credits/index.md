---
source_url: "https://openrouter.ai/docs/api/api-reference/credits/get-credits"
title: "Get remaining credits | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:54.991523+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Credits](index.md)

# Get remaining credits

GET

https://openrouter.ai/api/v1/credits

GET

/api/v1/credits

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/credits \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "total_credits": 100.5, |
| 4 | "total_usage": 25.75 |
| 5 | } |
| 6 | } |
```

Get total credits purchased and used for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Response

Returns the total credits purchased and used

dataobject

### Errors

401

Unauthorized Error

403

Forbidden Error

500

Internal Server Error
