---
source_url: "https://openrouter.ai/docs/api/api-reference/endpoints/list-endpoints"
title: "List all endpoints for a model | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:26.901577+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Endpoints](index.md)

# List all endpoints for a model

GET

https://openrouter.ai/api/v1/models/:author/:slug/endpoints

GET

/api/v1/models/:author/:slug/endpoints

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/models/openai/gpt-4/endpoints \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "id": "openai/gpt-4", |
| 4 | "name": "GPT-4", |
| 5 | "created": 1692901234, |
| 6 | "description": "GPT-4 is a large multimodal model.", |
| 7 | "architecture": { |
| 8 | "input_modalities": [ |
| 9 | "text" |
| 10 | ], |
| 11 | "instruct_type": "chatml", |
| 12 | "modality": "text->text", |
| 13 | "output_modalities": [ |
| 14 | "text" |
| 15 | ], |
| 16 | "tokenizer": "GPT" |
| 17 | }, |
| 18 | "endpoints": [] |
| 19 | } |
| 20 | } |
```

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Path parameters

authorstringRequired

The author/organization of the model

slugstringRequired

The model slug

### Response

Returns a list of endpoints

dataobject

List of available endpoints for a model

### Errors

404

Not Found Error

500

Internal Server Error
