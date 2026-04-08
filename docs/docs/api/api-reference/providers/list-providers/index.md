---
source_url: "https://openrouter.ai/docs/api/api-reference/providers/list-providers"
title: "List all providers | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.952914+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Providers](index.md)

# List all providers

GET

https://openrouter.ai/api/v1/providers

GET

/api/v1/providers

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/providers \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "name": "OpenAI", |
| 5 | "slug": "openai", |
| 6 | "privacy_policy_url": "https://openai.com/privacy", |
| 7 | "terms_of_service_url": "https://openai.com/terms", |
| 8 | "status_page_url": "https://status.openai.com", |
| 9 | "headquarters": "US", |
| 10 | "datacenters": [ |
| 11 | "US", |
| 12 | "IE" |
| 13 | ] |
| 14 | } |
| 15 | ] |
| 16 | } |
```

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Response

Returns a list of providers

datalist of objects

### Errors

500

Internal Server Error
