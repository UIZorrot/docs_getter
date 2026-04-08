---
source_url: "https://openrouter.ai/docs/api/api-reference/rerank/create-rerank"
title: "Submit a rerank request | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:28.123010+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Rerank](index.md)

# Submit a rerank request

POST

https://openrouter.ai/api/v1/rerank

POST

/api/v1/rerank

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/rerank \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "model": "cohere/rerank-v3.5", |
| 6 | "query": "What is the capital of France?", |
| 7 | "documents": [ |
| 8 | "Paris is the capital of France.", |
| 9 | "Berlin is the capital of Germany.", |
| 10 | "Madrid is the capital of Spain." |
| 11 | ] |
| 12 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "cohere/rerank-v3.5", |
| 3 | "results": [ |
| 4 | { |
| 5 | "index": 0, |
| 6 | "relevance_score": 0.98, |
| 7 | "document": { |
| 8 | "text": "Paris is the capital of France." |
| 9 | } |
| 10 | } |
| 11 | ], |
| 12 | "id": "gen-rerank-1234567890-abc", |
| 13 | "usage": { |
| 14 | "total_tokens": 150, |
| 15 | "search_units": 1 |
| 16 | } |
| 17 | } |
```

Submits a rerank request to the rerank router

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

modelstringRequired

The rerank model to use

querystringRequired

The search query to rerank documents against

documentslist of stringsRequired

The list of documents to rerank

top\_nintegerOptional`>=0`

Number of most relevant documents to return

providerobjectOptional

### Response

Rerank response

modelstring

The model used for reranking

resultslist of objects

List of rerank results sorted by relevance

idstring

Unique identifier for the rerank response (ORID format)

providerstring

The provider that served the rerank request

usageobject

Usage statistics

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
