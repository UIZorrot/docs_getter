---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/rerank"
title: "Rerank | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:44.815452+00:00"
---
[Python SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Rerank - Python SDK

Rerank method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

Reranking endpoints

### Available Operations

- [rerank](#rerank) - Submit a rerank request

## rerank

Submits a rerank request to the rerank router

### Example Usage

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | http_referer="<value>", |
| 6 | x_open_router_title="<value>", |
| 7 | x_open_router_categories="<value>", |
| 8 | api_key=os.getenv("OPENROUTER_API_KEY", ""), |
| 9 | ) as open_router: |
| 10 |  |
| 11 | res = open_router.rerank.rerank(model="cohere/rerank-v3.5", query="What is the capital of France?", documents=[ |
| 12 | "Paris is the capital of France.", |
| 13 | "Berlin is the capital of Germany.", |
| 14 | "Madrid is the capital of Spain.", |
| 15 | ]) |
| 16 |  |
| 17 | # Handle response |
| 18 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `model` | *str* | ✔️ | The rerank model to use | cohere/rerank-v3.5 |
| `query` | *str* | ✔️ | The search query to rerank documents against | What is the capital of France? |
| `documents` | List[*str*] | ✔️ | The list of documents to rerank | [ “Paris is the capital of France.”, “Berlin is the capital of Germany.” ] |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `top_n` | *Optional[int]* | ➖ | Number of most relevant documents to return | 3 |
| `provider` | [OptionalNullable[components.ProviderPreferences]](../../../components/providerpreferences.md/index.md) | ➖ | N/A | `{"allow_fallbacks": true}` |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.CreateRerankResponse](../operations/creatererankresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.PaymentRequiredResponseError | 402 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.BadGatewayResponseError | 502 | application/json |
| errors.ServiceUnavailableResponseError | 503 | application/json |
| errors.EdgeNetworkTimeoutResponseError | 524 | application/json |
| errors.ProviderOverloadedResponseError | 529 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
