---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/guardrails"
title: "Guardrails | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:44.650763+00:00"
---
[Python SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Guardrails - Python SDK

Guardrails method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

Guardrails endpoints

### Available Operations

- [list](#list) - List guardrails
- [create](#create) - Create a guardrail
- [get](#get) - Get a guardrail
- [update](#update) - Update a guardrail
- [delete](#delete) - Delete a guardrail
- [list\_key\_assignments](#list_key_assignments) - List all key assignments
- [list\_member\_assignments](#list_member_assignments) - List all member assignments
- [list\_guardrail\_key\_assignments](#list_guardrail_key_assignments) - List key assignments for a guardrail
- [bulk\_assign\_keys](#bulk_assign_keys) - Bulk assign keys to a guardrail
- [list\_guardrail\_member\_assignments](#list_guardrail_member_assignments) - List member assignments for a guardrail
- [bulk\_assign\_members](#bulk_assign_members) - Bulk assign members to a guardrail
- [bulk\_unassign\_keys](#bulk_unassign_keys) - Bulk unassign keys from a guardrail
- [bulk\_unassign\_members](#bulk_unassign_members) - Bulk unassign members from a guardrail

## list

List all guardrails for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.list() |
| 12 |  |
| 13 | while res is not None: |
| 14 | # Handle items |
| 15 |  |
| 16 | res = res.next() |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `offset` | *Optional[int]* | ➖ | Number of records to skip for pagination | 0 |
| `limit` | *Optional[int]* | ➖ | Maximum number of records to return (max 100) | 50 |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.ListGuardrailsResponse](../operations/listguardrailsresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## create

Create a new guardrail for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.create(name="My New Guardrail", description="A guardrail for limiting API usage", limit_usd=50, reset_interval="monthly", allowed_providers=[ |
| 12 | "openai", |
| 13 | "anthropic", |
| 14 | "deepseek", |
| 15 | ], ignored_providers=None, allowed_models=None, enforce_zdr=False) |
| 16 |  |
| 17 | # Handle response |
| 18 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `name` | *str* | ✔️ | Name for the new guardrail | My New Guardrail |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `description` | *OptionalNullable[str]* | ➖ | Description of the guardrail | A guardrail for limiting API usage |
| `limit_usd` | *Optional[float]* | ➖ | Spending limit in USD | 50 |
| `reset_interval` | [OptionalNullable[components.GuardrailInterval]](../../../components/guardrailinterval.md/index.md) | ➖ | Interval at which the limit resets (daily, weekly, monthly) | monthly |
| `allowed_providers` | List[*str*] | ➖ | List of allowed provider IDs | [ “openai”, “anthropic”, “deepseek” ] |
| `ignored_providers` | List[*str*] | ➖ | List of provider IDs to exclude from routing | [ “azure” ] |
| `allowed_models` | List[*str*] | ➖ | Array of model identifiers (slug or canonical\_slug accepted) | [ “openai/gpt-5.2”, “anthropic/claude-4.5-opus-20251124”, “deepseek/deepseek-r1-0528:free” ] |
| `enforce_zdr` | *OptionalNullable[bool]* | ➖ | Whether to enforce zero data retention | false |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.CreateGuardrailResponse](../components/createguardrailresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## get

Get a single guardrail by ID. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.get(id="550e8400-e29b-41d4-a716-446655440000") |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *str* | ✔️ | The unique identifier of the guardrail to retrieve | 550e8400-e29b-41d4-a716-446655440000 |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.GetGuardrailResponse](../components/getguardrailresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## update

Update an existing guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.update(id="550e8400-e29b-41d4-a716-446655440000", name="Updated Guardrail Name", description="Updated description", limit_usd=75, reset_interval="weekly") |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *str* | ✔️ | The unique identifier of the guardrail to update | 550e8400-e29b-41d4-a716-446655440000 |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `name` | *Optional[str]* | ➖ | New name for the guardrail | Updated Guardrail Name |
| `description` | *OptionalNullable[str]* | ➖ | New description for the guardrail | Updated description |
| `limit_usd` | *Optional[float]* | ➖ | New spending limit in USD | 75 |
| `reset_interval` | [OptionalNullable[components.GuardrailInterval]](../../../components/guardrailinterval.md/index.md) | ➖ | Interval at which the limit resets (daily, weekly, monthly) | monthly |
| `allowed_providers` | List[*str*] | ➖ | New list of allowed provider IDs | [ “openai”, “anthropic”, “deepseek” ] |
| `ignored_providers` | List[*str*] | ➖ | List of provider IDs to exclude from routing | [ “azure” ] |
| `allowed_models` | List[*str*] | ➖ | Array of model identifiers (slug or canonical\_slug accepted) | [ “openai/gpt-5.2” ] |
| `enforce_zdr` | *OptionalNullable[bool]* | ➖ | Whether to enforce zero data retention | true |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.UpdateGuardrailResponse](../components/updateguardrailresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## delete

Delete an existing guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.delete(id="550e8400-e29b-41d4-a716-446655440000") |
| 12 |  |
| 13 | # Handle response |
| 14 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *str* | ✔️ | The unique identifier of the guardrail to delete | 550e8400-e29b-41d4-a716-446655440000 |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.DeleteGuardrailResponse](../components/deleteguardrailresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## list\_key\_assignments

List all API key guardrail assignments for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.list_key_assignments() |
| 12 |  |
| 13 | while res is not None: |
| 14 | # Handle items |
| 15 |  |
| 16 | res = res.next() |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `offset` | *Optional[int]* | ➖ | Number of records to skip for pagination | 0 |
| `limit` | *Optional[int]* | ➖ | Maximum number of records to return (max 100) | 50 |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.ListKeyAssignmentsResponse](../operations/listkeyassignmentsresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## list\_member\_assignments

List all organization member guardrail assignments for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.list_member_assignments() |
| 12 |  |
| 13 | while res is not None: |
| 14 | # Handle items |
| 15 |  |
| 16 | res = res.next() |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `offset` | *Optional[int]* | ➖ | Number of records to skip for pagination | 0 |
| `limit` | *Optional[int]* | ➖ | Maximum number of records to return (max 100) | 50 |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.ListMemberAssignmentsResponse](../operations/listmemberassignmentsresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## list\_guardrail\_key\_assignments

List all API key assignments for a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.list_guardrail_key_assignments(id="550e8400-e29b-41d4-a716-446655440000") |
| 12 |  |
| 13 | while res is not None: |
| 14 | # Handle items |
| 15 |  |
| 16 | res = res.next() |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *str* | ✔️ | The unique identifier of the guardrail | 550e8400-e29b-41d4-a716-446655440000 |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `offset` | *Optional[int]* | ➖ | Number of records to skip for pagination | 0 |
| `limit` | *Optional[int]* | ➖ | Maximum number of records to return (max 100) | 50 |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.ListGuardrailKeyAssignmentsResponse](../operations/listguardrailkeyassignmentsresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## bulk\_assign\_keys

Assign multiple API keys to a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.bulk_assign_keys(id="550e8400-e29b-41d4-a716-446655440000", key_hashes=[ |
| 12 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 13 | ]) |
| 14 |  |
| 15 | # Handle response |
| 16 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *str* | ✔️ | The unique identifier of the guardrail | 550e8400-e29b-41d4-a716-446655440000 |
| `key_hashes` | List[*str*] | ✔️ | Array of API key hashes to assign to the guardrail | [ “c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93” ] |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.BulkAssignKeysResponse](../components/bulkassignkeysresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## list\_guardrail\_member\_assignments

List all organization member assignments for a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.list_guardrail_member_assignments(id="550e8400-e29b-41d4-a716-446655440000") |
| 12 |  |
| 13 | while res is not None: |
| 14 | # Handle items |
| 15 |  |
| 16 | res = res.next() |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *str* | ✔️ | The unique identifier of the guardrail | 550e8400-e29b-41d4-a716-446655440000 |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `offset` | *Optional[int]* | ➖ | Number of records to skip for pagination | 0 |
| `limit` | *Optional[int]* | ➖ | Maximum number of records to return (max 100) | 50 |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.ListGuardrailMemberAssignmentsResponse](../operations/listguardrailmemberassignmentsresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## bulk\_assign\_members

Assign multiple organization members to a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.bulk_assign_members(id="550e8400-e29b-41d4-a716-446655440000", member_user_ids=[ |
| 12 | "user_abc123", |
| 13 | "user_def456", |
| 14 | ]) |
| 15 |  |
| 16 | # Handle response |
| 17 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *str* | ✔️ | The unique identifier of the guardrail | 550e8400-e29b-41d4-a716-446655440000 |
| `member_user_ids` | List[*str*] | ✔️ | Array of member user IDs to assign to the guardrail | [ “user\_abc123”, “user\_def456” ] |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.BulkAssignMembersResponse](../components/bulkassignmembersresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## bulk\_unassign\_keys

Unassign multiple API keys from a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.bulk_unassign_keys(id="550e8400-e29b-41d4-a716-446655440000", key_hashes=[ |
| 12 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 13 | ]) |
| 14 |  |
| 15 | # Handle response |
| 16 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *str* | ✔️ | The unique identifier of the guardrail | 550e8400-e29b-41d4-a716-446655440000 |
| `key_hashes` | List[*str*] | ✔️ | Array of API key hashes to unassign from the guardrail | [ “c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93” ] |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.BulkUnassignKeysResponse](../components/bulkunassignkeysresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## bulk\_unassign\_members

Unassign multiple organization members from a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.guardrails.bulk_unassign_members(id="550e8400-e29b-41d4-a716-446655440000", member_user_ids=[ |
| 12 | "user_abc123", |
| 13 | "user_def456", |
| 14 | ]) |
| 15 |  |
| 16 | # Handle response |
| 17 | print(res) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *str* | ✔️ | The unique identifier of the guardrail | 550e8400-e29b-41d4-a716-446655440000 |
| `member_user_ids` | List[*str*] | ✔️ | Array of member user IDs to unassign from the guardrail | [ “user\_abc123”, “user\_def456” ] |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.BulkUnassignMembersResponse](../components/bulkunassignmembersresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
