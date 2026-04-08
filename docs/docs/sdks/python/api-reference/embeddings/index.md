---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/embeddings"
title: "Embeddings | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:44.097373+00:00"
---
[Python SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Embeddings - Python SDK

Embeddings method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

Text embedding endpoints

### Available Operations

- [generate](#generate) - Submit an embedding request
- [list\_models](#list_models) - List all embeddings models

## generate

Submits an embedding request to the embeddings router

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
| 11 | res = open_router.embeddings.generate(input="The quick brown fox jumps over the lazy dog", model="openai/text-embedding-3-small") |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `input` | [operations.InputUnion](../operations/inputunion/index.md) | ✔️ | Text, token, or multimodal input(s) to embed | The quick brown fox jumps over the lazy dog |
| `model` | *str* | ✔️ | The model to use for embeddings | openai/text-embedding-3-small |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `encoding_format` | [Optional[operations.EncodingFormat]](../../../operations/encodingformat.md/index.md) | ➖ | The format of the output embeddings | float |
| `dimensions` | *Optional[int]* | ➖ | The number of dimensions for the output embeddings | 1536 |
| `user` | *Optional[str]* | ➖ | A unique identifier for the end-user | user-1234 |
| `provider` | [OptionalNullable[components.ProviderPreferences]](../../../components/providerpreferences.md/index.md) | ➖ | N/A | `{"allow_fallbacks": true}` |
| `input_type` | *Optional[str]* | ➖ | The type of input (e.g. search\_query, search\_document) | search\_query |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.CreateEmbeddingsResponse](../operations/createembeddingsresponse/index.md)**

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

## list\_models

Returns a list of all available embeddings models and their properties

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
| 11 | res = open_router.embeddings.list_models() |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |

### Response

**[components.ModelsListResponse](../components/modelslistresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
