---
source_url: "https://openrouter.ai/docs/api/api-reference/models/list-models-count"
title: "Get total count of available models | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:27.541502+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Models](index.md)

# Get total count of available models

GET

https://openrouter.ai/api/v1/models/count

GET

/api/v1/models/count

```
|  |  |
| --- | --- |
| 1 | curl https://openrouter.ai/api/v1/models/count \ |
| 2 | -H "Authorization: Bearer <token>" |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "data": { |
| 3 | "count": 150 |
| 4 | } |
| 5 | } |
```

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Query parameters

output\_modalitiesstringOptional

Filter models by output modality. Accepts a comma-separated list of modalities (text, image, audio, embeddings) or “all” to include all models. Defaults to “text”.

### Response

Returns the total count of available models

dataobject

Model count data

### Errors

400

Bad Request Error

500

Internal Server Error
