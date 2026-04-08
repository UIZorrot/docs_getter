---
source_url: "https://openrouter.ai/docs/api/api-reference/embeddings/list-embeddings-models"
title: "List all embeddings models | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:26.664751+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Embeddings](../create-embeddings/index.md)

# List all embeddings models

GET

https://openrouter.ai/api/v1/embeddings/models

GET

/api/v1/embeddings/models

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/embeddings/models \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": [ |
| 3 | { |
| 4 | "id": "openai/text-embedding-3-small", |
| 5 | "canonical_slug": "openai/text-embedding-3-small", |
| 6 | "name": "Text Embedding 3 Small", |
| 7 | "created": 1692901234, |
| 8 | "pricing": { |
| 9 | "prompt": "0.00000002", |
| 10 | "completion": "0", |
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
| 21 | "embeddings" |
| 22 | ], |
| 23 | "tokenizer": "GPT" |
| 24 | }, |
| 25 | "top_provider": { |
| 26 | "is_moderated": false, |
| 27 | "context_length": 8192 |
| 28 | }, |
| 29 | "supported_parameters": [], |
| 30 | "links": { |
| 31 | "details": "/api/v1/models/openai/text-embedding-3-small/endpoints" |
| 32 | }, |
| 33 | "description": "OpenAI text embedding model optimized for performance." |
| 34 | } |
| 35 | ] |
| 36 | } |
```

Returns a list of all available embeddings models and their properties

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Response

Returns a list of embeddings models

datalist of objects

List of available models

### Errors

400

Bad Request Error

500

Internal Server Error
