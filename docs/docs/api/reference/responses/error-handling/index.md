---
source_url: "https://openrouter.ai/docs/api/reference/responses/error-handling"
title: "Responses API Beta Error Handling | Basic Error Guide | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:30.277956+00:00"
---
[API Guides](../../overview/index.md)[Responses API](../overview/index.md)

# Error Handling

Understanding and handling errors in the Responses API Beta

##### Beta API

This API is in **beta stage** and may have breaking changes. Use with caution in production environments.

##### Stateless Only

This API is **stateless** - each request is independent and no conversation state is persisted between requests. You must include the full conversation history in each request.

The Responses API Beta returns structured error responses that follow a consistent format.

## Error Response Format

All errors follow this structure:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "error": { |
| 3 | "code": "invalid_prompt", |
| 4 | "message": "Detailed error description" |
| 5 | }, |
| 6 | "metadata": null |
| 7 | } |
```

### Error Codes

The API uses the following error codes:

| Code | Description | Equivalent HTTP Status |
| --- | --- | --- |
| `invalid_prompt` | Request validation failed | 400 |
| `rate_limit_exceeded` | Too many requests | 429 |
| `server_error` | Internal server error | 500+ |
