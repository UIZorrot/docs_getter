---
source_url: "https://openrouter.ai/docs/api/api-reference/embeddings/create-embeddings"
title: "Submit an embedding request | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:52.020340+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Embeddings](index.md)

# Submit an embedding request

POST

https://openrouter.ai/api/v1/embeddings

POST

/api/v1/embeddings

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/embeddings \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "input": "The quick brown fox jumps over the lazy dog", |
| 6 | "model": "openai/text-embedding-3-small" |
| 7 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "object": "list", |
| 3 | "data": [ |
| 4 | { |
| 5 | "object": "embedding", |
| 6 | "embedding": [ |
| 7 | 0.0023064255, |
| 8 | -0.009327292, |
| 9 | 0.015797347 |
| 10 | ], |
| 11 | "index": 0 |
| 12 | } |
| 13 | ], |
| 14 | "model": "openai/text-embedding-3-small", |
| 15 | "usage": { |
| 16 | "prompt_tokens": 8, |
| 17 | "total_tokens": 8 |
| 18 | } |
| 19 | } |
```

Submits an embedding request to the embeddings router

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

inputstring or list of strings or list of doubles or list of lists of doubles or list of objectsRequired

Text, token, or multimodal input(s) to embed

modelstringRequired

The model to use for embeddings

encoding\_formatenumOptional

The format of the output embeddings

Allowed values:

dimensionsintegerOptional`>=0`

The number of dimensions for the output embeddings

userstringOptional

A unique identifier for the end-user

providerobjectOptional

input\_typestringOptional

The type of input (e.g. search\_query, search\_document)

### Response

Embedding response

objectenum

Allowed values:

datalist of objects

List of embedding objects

modelstring

The model used for embeddings

idstring

Unique identifier for the embeddings response

usageobject

Token usage statistics

### Errors

400

Bad Request Error

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

503

Service Unavailable Error
