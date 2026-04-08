---
source_url: "https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints-zdr"
title: "Preview the impact of ZDR on the available endpoints | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:26.466147+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Endpoints](../list-endpoints/index.md)

# Preview the impact of ZDR on the available endpoints

GET

https://openrouter.ai/api/v1/endpoints/zdr

GET

/api/v1/endpoints/zdr

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/endpoints/zdr \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "name": "OpenAI: GPT-4", |
| 5 | "model_id": "openai/gpt-4", |
| 6 | "model_name": "GPT-4", |
| 7 | "context_length": 8192, |
| 8 | "pricing": { |
| 9 | "prompt": "0.00003", |
| 10 | "completion": "0.00006", |
| 11 | "request": "0", |
| 12 | "image": "0" |
| 13 | }, |
| 14 | "provider_name": "OpenAI", |
| 15 | "tag": "openai", |
| 16 | "quantization": "fp16", |
| 17 | "max_completion_tokens": 4096, |
| 18 | "max_prompt_tokens": 8192, |
| 19 | "supported_parameters": [ |
| 20 | "temperature", |
| 21 | "top_p", |
| 22 | "max_tokens" |
| 23 | ], |
| 24 | "uptime_last_30m": 99.5, |
| 25 | "uptime_last_5m": 100, |
| 26 | "uptime_last_1d": 99.8, |
| 27 | "supports_implicit_caching": true, |
| 28 | "latency_last_30m": { |
| 29 | "p50": 0.25, |
| 30 | "p75": 0.35, |
| 31 | "p90": 0.48, |
| 32 | "p99": 0.85 |
| 33 | }, |
| 34 | "throughput_last_30m": { |
| 35 | "p50": 45.2, |
| 36 | "p75": 38.5, |
| 37 | "p90": 28.3, |
| 38 | "p99": 15.1 |
| 39 | }, |
| 40 | "status": 0 |
| 41 | } |
| 42 | ] |
| 43 | } |
```

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Response

Returns a list of endpoints

datalist of objects

### Errors

500

Internal Server Error
