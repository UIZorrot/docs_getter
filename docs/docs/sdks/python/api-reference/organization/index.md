---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/organization"
title: "Organization | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:45.082657+00:00"
---
[Python SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Organization - Python SDK

Organization method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

Organization endpoints

### Available Operations

- [list\_members](#list_members) - List organization members

## list\_members

List all members of the organization associated with the authenticated management key. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | res = open_router.organization.list_members() |
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

**[operations.ListOrganizationMembersResponse](../operations/listorganizationmembersresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
