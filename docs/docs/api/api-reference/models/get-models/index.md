---
source_url: "https://openrouter.ai/docs/api/api-reference/models/get-models"
title: "List all models and their properties | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:56.446499+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Models](../list-models-count/index.md)

# List all models and their properties

GET

https://openrouter.ai/api/v1/models

GET

/api/v1/models

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/models \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "id": "openai/gpt-4", |
| 5 | "canonical_slug": "openai/gpt-4", |
| 6 | "name": "GPT-4", |
| 7 | "created": 1692901234, |
| 8 | "pricing": { |
| 9 | "prompt": "0.00003", |
| 10 | "completion": "0.00006", |
| 11 | "request": "0", |
| 12 | "image": "0" |
| 13 | }, |
| 14 | "context_length": 8192, |
| 15 | "architecture": { |
| 16 | "modality": "text->text", |
| 17 | "input_modalities": [ |
| 18 | "text" |
| 19 | ], |
| 20 | "output_modalities": [ |
| 21 | "text" |
| 22 | ], |
| 23 | "tokenizer": "GPT", |
| 24 | "instruct_type": "chatml" |
| 25 | }, |
| 26 | "top_provider": { |
| 27 | "is_moderated": true, |
| 28 | "context_length": 8192, |
| 29 | "max_completion_tokens": 4096 |
| 30 | }, |
| 31 | "supported_parameters": [ |
| 32 | "temperature", |
| 33 | "top_p", |
| 34 | "max_tokens" |
| 35 | ], |
| 36 | "links": { |
| 37 | "details": "/api/v1/models/openai/gpt-5.4/endpoints" |
| 38 | }, |
| 39 | "description": "GPT-4 is a large multimodal model that can solve difficult problems with greater accuracy." |
| 40 | } |
| 41 | ] |
| 42 | } |
```

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

categoryenumOptional

Filter models by use case category

supported\_parametersstringOptional

Filter models by supported parameter (comma-separated)

output\_modalitiesstringOptional

Filter models by output modality. Accepts a comma-separated list of modalities (text, image, audio, embeddings) or “all” to include all models. Defaults to “text”.

use\_rssstringOptional

Return results as RSS feed

use\_rss\_chat\_linksstringOptional

Use chat links in RSS feed items

### Response

Returns a list of models or RSS feed

datalist of objects

List of available models

### Errors

400

Bad Request Error

500

Internal Server Error
