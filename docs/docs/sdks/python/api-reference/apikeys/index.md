---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/apikeys"
title: "APIKeys | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:43.724917+00:00"
---
[Python SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

APIKeys - Python SDK

APIKeys method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

API key management endpoints

### Available Operations

- [list](#list) - List API keys
- [create](#create) - Create a new API key
- [update](#update) - Update an API key
- [delete](#delete) - Delete an API key
- [get](#get) - Get a single API key
- [get\_current\_key\_metadata](#get_current_key_metadata) - Get current API key

## list

List all API keys for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.api_keys.list() |
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
| `include_disabled` | *Optional[str]* | ➖ | Whether to include disabled API keys in the response | false |
| `offset` | *Optional[int]* | ➖ | Number of API keys to skip for pagination | 0 |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.ListResponse](../operations/listresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## create

Create a new API key for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Example Usage

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | from openrouter.utils import parse_datetime |
| 3 | import os |
| 4 |  |
| 5 | with OpenRouter( |
| 6 | http_referer="<value>", |
| 7 | x_open_router_title="<value>", |
| 8 | x_open_router_categories="<value>", |
| 9 | api_key=os.getenv("OPENROUTER_API_KEY", ""), |
| 10 | ) as open_router: |
| 11 |  |
| 12 | res = open_router.api_keys.create(name="My New API Key", limit=50, limit_reset="monthly", include_byok_in_limit=True, expires_at=parse_datetime("2027-12-31T23:59:59Z")) |
| 13 |  |
| 14 | # Handle response |
| 15 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `name` | *str* | ✔️ | Name for the new API key | My New API Key |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `limit` | *Optional[float]* | ➖ | Optional spending limit for the API key in USD | 50 |
| `limit_reset` | [OptionalNullable[operations.CreateKeysLimitReset]](../../../operations/createkeyslimitreset.md/index.md) | ➖ | Type of limit reset for the API key (daily, weekly, monthly, or null for no reset). Resets happen automatically at midnight UTC, and weeks are Monday through Sunday. | monthly |
| `include_byok_in_limit` | *Optional[bool]* | ➖ | Whether to include BYOK usage in the limit | true |
| `expires_at` | [date](https://docs.python.org/3/library/datetime.html) | ➖ | Optional ISO 8601 UTC timestamp when the API key should expire. Must be UTC, other timezones will be rejected | 2027-12-31T23:59:59Z |
| `creator_user_id` | *OptionalNullable[str]* | ➖ | Optional user ID of the key creator. Only meaningful for organization-owned keys where a specific member is creating the key. | user\_2dHFtVWx2n56w6HkM0000000000 |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.CreateKeysResponse](../operations/createkeysresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## update

Update an existing API key. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.api_keys.update(hash="f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943", name="Updated API Key Name", disabled=False, limit=75, limit_reset="daily", include_byok_in_limit=True) |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `hash` | *str* | ✔️ | The hash identifier of the API key to update | f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943 |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `name` | *Optional[str]* | ➖ | New name for the API key | Updated API Key Name |
| `disabled` | *Optional[bool]* | ➖ | Whether to disable the API key | false |
| `limit` | *Optional[float]* | ➖ | New spending limit for the API key in USD | 75 |
| `limit_reset` | [OptionalNullable[operations.UpdateKeysLimitReset]](../../../operations/updatekeyslimitreset.md/index.md) | ➖ | New limit reset type for the API key (daily, weekly, monthly, or null for no reset). Resets happen automatically at midnight UTC, and weeks are Monday through Sunday. | daily |
| `include_byok_in_limit` | *Optional[bool]* | ➖ | Whether to include BYOK usage in the limit | true |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.UpdateKeysResponse](../operations/updatekeysresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## delete

Delete an existing API key. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.api_keys.delete(hash="f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943") |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `hash` | *str* | ✔️ | The hash identifier of the API key to delete | f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943 |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.DeleteKeysResponse](../operations/deletekeysresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## get

Get a single API key by hash. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.api_keys.get(hash="f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943") |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `hash` | *str* | ✔️ | The hash identifier of the API key to retrieve | f01d52606dc8f0a8303a7b5cc3fa07109c2e346cec7c0a16b40de462992ce943 |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.GetKeyResponse](../operations/getkeyresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## get\_current\_key\_metadata

Get information on the API key associated with the current authentication session

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
| 11 | res = open_router.api_keys.get_current_key_metadata() |
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

**[operations.GetCurrentKeyResponse](../operations/getcurrentkeyresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
