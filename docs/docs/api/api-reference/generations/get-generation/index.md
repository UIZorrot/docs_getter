---
source_url: "https://openrouter.ai/docs/api/api-reference/generations/get-generation"
title: "Get request & usage metadata for a generation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:52.229551+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Generations](index.md)

# 

Get request & usage metadata for a generation

GET

https://openrouter.ai/api/v1/generation

GET

/api/v1/generation

```
|  |  |
| --- | --- |
| 1 | curl -G https://openrouter.ai/api/v1/generation \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -d id=gen-1234567890 |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "id": "gen-3bhGkxlo4XFrqiabUM7NDtwDzWwG", |
| 4 | "upstream_id": "chatcmpl-791bcf62-080e-4568-87d0-94c72e3b4946", |
| 5 | "total_cost": 0.0015, |
| 6 | "cache_discount": 0.0002, |
| 7 | "upstream_inference_cost": 0.0012, |
| 8 | "created_at": "2024-07-15T23:33:19.433273+00:00", |
| 9 | "model": "sao10k/l3-stheno-8b", |
| 10 | "app_id": 12345, |
| 11 | "streamed": true, |
| 12 | "cancelled": false, |
| 13 | "provider_name": "Infermatic", |
| 14 | "latency": 1250, |
| 15 | "moderation_latency": 50, |
| 16 | "generation_time": 1200, |
| 17 | "finish_reason": "stop", |
| 18 | "tokens_prompt": 10, |
| 19 | "tokens_completion": 25, |
| 20 | "native_tokens_prompt": 10, |
| 21 | "native_tokens_completion": 25, |
| 22 | "native_tokens_completion_images": 0, |
| 23 | "native_tokens_reasoning": 5, |
| 24 | "native_tokens_cached": 3, |
| 25 | "num_media_prompt": 1, |
| 26 | "num_input_audio_prompt": 0, |
| 27 | "num_media_completion": 0, |
| 28 | "num_search_results": 5, |
| 29 | "origin": "https://openrouter.ai/", |
| 30 | "usage": 0.0015, |
| 31 | "is_byok": false, |
| 32 | "native_finish_reason": "stop", |
| 33 | "external_user": "user-123", |
| 34 | "request_id": "req-1727282430-aBcDeFgHiJkLmNoPqRsT" |
| 35 | } |
| 36 | } |
```

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

idstringRequired`>=1 character`

The generation ID

### Response

Returns the request metadata for this generation

dataobject

Generation data

### Errors

401

Unauthorized Error

402

Payment Required Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error

502

Bad Gateway Error
