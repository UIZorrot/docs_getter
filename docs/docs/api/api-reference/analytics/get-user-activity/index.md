---
source_url: "https://openrouter.ai/docs/api/api-reference/analytics/get-user-activity"
title: "Get user activity grouped by endpoint | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:25.215586+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Analytics](index.md)

# Get user activity grouped by endpoint

GET

https://openrouter.ai/api/v1/activity

GET

/api/v1/activity

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/activity \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "date": "2025-08-24", |
| 5 | "model": "openai/gpt-4.1", |
| 6 | "model_permaslug": "openai/gpt-4.1-2025-04-14", |
| 7 | "endpoint_id": "550e8400-e29b-41d4-a716-446655440000", |
| 8 | "provider_name": "OpenAI", |
| 9 | "usage": 0.015, |
| 10 | "byok_usage_inference": 0.012, |
| 11 | "requests": 5, |
| 12 | "prompt_tokens": 50, |
| 13 | "completion_tokens": 125, |
| 14 | "reasoning_tokens": 25 |
| 15 | } |
| 16 | ] |
| 17 | } |
```

Returns user activity data grouped by endpoint for the last 30 (completed) UTC days. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

datestringOptional

Filter by a single UTC date in the last 30 days (YYYY-MM-DD format).

api\_key\_hashstringOptional

Filter by API key hash (SHA-256 hex string, as returned by the keys API).

user\_idstringOptional

Filter by org member user ID. Only applicable for organization accounts.

### Response

Returns user activity data grouped by endpoint

datalist of objects

List of activity items

### Errors

400

Bad Request Error

401

Unauthorized Error

403

Forbidden Error

404

Not Found Error

500

Internal Server Error
