---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/analytics"
title: "Analytics | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:43.522839+00:00"
---
[Python SDK](../../overview/index.md)[API Reference](index.md)

# 

Analytics - Python SDK

Analytics method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

Analytics and usage endpoints

### Available Operations

- [get\_user\_activity](#get_user_activity) - Get user activity grouped by endpoint

## get\_user\_activity

Returns user activity data grouped by endpoint for the last 30 (completed) UTC days. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.analytics.get_user_activity() |
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
| `date_` | *Optional[str]* | ➖ | Filter by a single UTC date in the last 30 days (YYYY-MM-DD format). | 2025-08-24 |
| `api_key_hash` | *Optional[str]* | ➖ | Filter by API key hash (SHA-256 hex string, as returned by the keys API). | abc123def456… |
| `user_id` | *Optional[str]* | ➖ | Filter by org member user ID. Only applicable for organization accounts. | user\_abc123 |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[components.ActivityResponse](../components/activityresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.ForbiddenResponseError | 403 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
