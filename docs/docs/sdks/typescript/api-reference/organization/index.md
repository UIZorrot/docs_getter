---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/organization"
title: "Organization | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:47.501464+00:00"
---
[TypeScript SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Organization - TypeScript SDK

Organization method reference

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Overview

Organization endpoints

### Available Operations

- [listMembers](#listmembers) - List organization members

## listMembers

List all members of the organization associated with the authenticated management key. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

### Example Usage

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from "@openrouter/sdk"; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | httpReferer: "<value>", |
| 5 | appTitle: "<value>", |
| 6 | appCategories: "<value>", |
| 7 | apiKey: process.env["OPENROUTER_API_KEY"] ?? "", |
| 8 | }); |
| 9 |  |
| 10 | async function run() { |
| 11 | const result = await openRouter.organization.listMembers(); |
| 12 |  |
| 13 | for await (const page of result) { |
| 14 | console.log(page); |
| 15 | } |
| 16 | } |
| 17 |  |
| 18 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { organizationListMembers } from "@openrouter/sdk/funcs/organizationListMembers.js"; |
| 3 |  |
| 4 | // Use `OpenRouterCore` for best tree-shaking performance. |
| 5 | // You can create one instance of it to use across an application. |
| 6 | const openRouter = new OpenRouterCore({ |
| 7 | httpReferer: "<value>", |
| 8 | appTitle: "<value>", |
| 9 | appCategories: "<value>", |
| 10 | apiKey: process.env["OPENROUTER_API_KEY"] ?? "", |
| 11 | }); |
| 12 |  |
| 13 | async function run() { |
| 14 | const res = await organizationListMembers(openRouter); |
| 15 | if (res.ok) { |
| 16 | const { value: result } = res; |
| 17 | for await (const page of result) { |
| 18 | console.log(page); |
| 19 | } |
| 20 | } else { |
| 21 | console.log("organizationListMembers failed:", res.error); |
| 22 | } |
| 23 | } |
| 24 |  |
| 25 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.ListOrganizationMembersRequest](../operations/listorganizationmembersrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.ListOrganizationMembersResponse](../operations/listorganizationmembersresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
