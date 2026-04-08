---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/models/models"
title: "Models | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:45.249265+00:00"
---
[Python SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](index.md)

# 

Models - Python SDK

Models method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

Model information endpoints

### Available Operations

- [count](#count) - Get total count of available models
- [list](#list) - List all models and their properties
- [list\_for\_user](#list_for_user) - List models filtered by user provider preferences, privacy settings, and guardrails

## count

Get total count of available models

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
| 11 | res = open_router.models.count() |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `output_modalities` | *Optional[str]* | ➖ | Filter models by output modality. Accepts a comma-separated list of modalities (text, image, audio, embeddings) or “all” to include all models. Defaults to “text”. | text |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.ModelsCountResponse](../../components/modelscountresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## list

List all models and their properties

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
| 11 | res = open_router.models.list() |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `category` | [Optional[operations.Category]](../../../operations/category.md/index.md) | ➖ | Filter models by use case category | programming |
| `supported_parameters` | *Optional[str]* | ➖ | Filter models by supported parameter (comma-separated) | temperature |
| `output_modalities` | *Optional[str]* | ➖ | Filter models by output modality. Accepts a comma-separated list of modalities (text, image, audio, embeddings) or “all” to include all models. Defaults to “text”. | text |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.ModelsListResponse](../../components/modelslistresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## list\_for\_user

List models filtered by user provider preferences, [privacy settings](../../../../../guides/privacy/logging/index.md), and [guardrails](../../../../../guides/features/guardrails/index.md). If requesting through `eu.openrouter.ai/api/v1/...` the results will be filtered to models that satisfy [EU in-region routing](../../../../../guides/privacy/logging/index.md).

### Example Usage

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter, operations |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | http_referer="<value>", |
| 6 | x_open_router_title="<value>", |
| 7 | x_open_router_categories="<value>", |
| 8 | ) as open_router: |
| 9 |  |
| 10 | res = open_router.models.list_for_user(security=operations.ListModelsUserSecurity( |
| 11 | bearer=os.getenv("OPENROUTER_BEARER", ""), |
| 12 | )) |
| 13 |  |
| 14 | # Handle response |
| 15 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `security` | [operations.ListModelsUserSecurity](../../operations/listmodelsusersecurity/index.md) | ✔️ | N/A |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |

### Response

**[components.ModelsListResponse](../../components/modelslistresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
