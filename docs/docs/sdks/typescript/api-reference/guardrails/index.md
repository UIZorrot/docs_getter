---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/guardrails"
title: "Guardrails | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:47.149834+00:00"
---
[TypeScript SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Guardrails - TypeScript SDK

Guardrails method reference

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Overview

Guardrails endpoints

### Available Operations

- [list](#list) - List guardrails
- [create](#create) - Create a guardrail
- [get](#get) - Get a guardrail
- [update](#update) - Update a guardrail
- [delete](#delete) - Delete a guardrail
- [listKeyAssignments](#listkeyassignments) - List all key assignments
- [listMemberAssignments](#listmemberassignments) - List all member assignments
- [listGuardrailKeyAssignments](#listguardrailkeyassignments) - List key assignments for a guardrail
- [bulkAssignKeys](#bulkassignkeys) - Bulk assign keys to a guardrail
- [listGuardrailMemberAssignments](#listguardrailmemberassignments) - List member assignments for a guardrail
- [bulkAssignMembers](#bulkassignmembers) - Bulk assign members to a guardrail
- [bulkUnassignKeys](#bulkunassignkeys) - Bulk unassign keys from a guardrail
- [bulkUnassignMembers](#bulkunassignmembers) - Bulk unassign members from a guardrail

## list

List all guardrails for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | const result = await openRouter.guardrails.list(); |
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
| 2 | import { guardrailsList } from "@openrouter/sdk/funcs/guardrailsList.js"; |
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
| 14 | const res = await guardrailsList(openRouter); |
| 15 | if (res.ok) { |
| 16 | const { value: result } = res; |
| 17 | for await (const page of result) { |
| 18 | console.log(page); |
| 19 | } |
| 20 | } else { |
| 21 | console.log("guardrailsList failed:", res.error); |
| 22 | } |
| 23 | } |
| 24 |  |
| 25 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.ListGuardrailsRequest](../operations/listguardrailsrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.ListGuardrailsResponse](../operations/listguardrailsresponse/index.md)>**

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
| 11 | const result = await openRouter.guardrails.create({ |
| 12 | createGuardrailRequest: { |
| 13 | name: "My New Guardrail", |
| 14 | description: "A guardrail for limiting API usage", |
| 15 | limitUsd: 50, |
| 16 | resetInterval: "monthly", |
| 17 | allowedProviders: [ |
| 18 | "openai", |
| 19 | "anthropic", |
| 20 | "deepseek", |
| 21 | ], |
| 22 | ignoredProviders: null, |
| 23 | allowedModels: null, |
| 24 | enforceZdr: false, |
| 25 | }, |
| 26 | }); |
| 27 |  |
| 28 | console.log(result); |
| 29 | } |
| 30 |  |
| 31 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { guardrailsCreate } from "@openrouter/sdk/funcs/guardrailsCreate.js"; |
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
| 14 | const res = await guardrailsCreate(openRouter, { |
| 15 | createGuardrailRequest: { |
| 16 | name: "My New Guardrail", |
| 17 | description: "A guardrail for limiting API usage", |
| 18 | limitUsd: 50, |
| 19 | resetInterval: "monthly", |
| 20 | allowedProviders: [ |
| 21 | "openai", |
| 22 | "anthropic", |
| 23 | "deepseek", |
| 24 | ], |
| 25 | ignoredProviders: null, |
| 26 | allowedModels: null, |
| 27 | enforceZdr: false, |
| 28 | }, |
| 29 | }); |
| 30 | if (res.ok) { |
| 31 | const { value: result } = res; |
| 32 | console.log(result); |
| 33 | } else { |
| 34 | console.log("guardrailsCreate failed:", res.error); |
| 35 | } |
| 36 | } |
| 37 |  |
| 38 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.CreateGuardrailRequest](../operations/createguardrailrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[models.CreateGuardrailResponse](../models/createguardrailresponse/index.md)>**

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
| 11 | const result = await openRouter.guardrails.get({ |
| 12 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 13 | }); |
| 14 |  |
| 15 | console.log(result); |
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
| 2 | import { guardrailsGet } from "@openrouter/sdk/funcs/guardrailsGet.js"; |
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
| 14 | const res = await guardrailsGet(openRouter, { |
| 15 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 16 | }); |
| 17 | if (res.ok) { |
| 18 | const { value: result } = res; |
| 19 | console.log(result); |
| 20 | } else { |
| 21 | console.log("guardrailsGet failed:", res.error); |
| 22 | } |
| 23 | } |
| 24 |  |
| 25 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.GetGuardrailRequest](../operations/getguardrailrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[models.GetGuardrailResponse](../models/getguardrailresponse/index.md)>**

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
| 11 | const result = await openRouter.guardrails.update({ |
| 12 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 13 | updateGuardrailRequest: { |
| 14 | name: "Updated Guardrail Name", |
| 15 | description: "Updated description", |
| 16 | limitUsd: 75, |
| 17 | resetInterval: "weekly", |
| 18 | }, |
| 19 | }); |
| 20 |  |
| 21 | console.log(result); |
| 22 | } |
| 23 |  |
| 24 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { guardrailsUpdate } from "@openrouter/sdk/funcs/guardrailsUpdate.js"; |
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
| 14 | const res = await guardrailsUpdate(openRouter, { |
| 15 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 16 | updateGuardrailRequest: { |
| 17 | name: "Updated Guardrail Name", |
| 18 | description: "Updated description", |
| 19 | limitUsd: 75, |
| 20 | resetInterval: "weekly", |
| 21 | }, |
| 22 | }); |
| 23 | if (res.ok) { |
| 24 | const { value: result } = res; |
| 25 | console.log(result); |
| 26 | } else { |
| 27 | console.log("guardrailsUpdate failed:", res.error); |
| 28 | } |
| 29 | } |
| 30 |  |
| 31 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.UpdateGuardrailRequest](../operations/updateguardrailrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[models.UpdateGuardrailResponse](../models/updateguardrailresponse/index.md)>**

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
| 11 | const result = await openRouter.guardrails.delete({ |
| 12 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 13 | }); |
| 14 |  |
| 15 | console.log(result); |
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
| 2 | import { guardrailsDelete } from "@openrouter/sdk/funcs/guardrailsDelete.js"; |
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
| 14 | const res = await guardrailsDelete(openRouter, { |
| 15 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 16 | }); |
| 17 | if (res.ok) { |
| 18 | const { value: result } = res; |
| 19 | console.log(result); |
| 20 | } else { |
| 21 | console.log("guardrailsDelete failed:", res.error); |
| 22 | } |
| 23 | } |
| 24 |  |
| 25 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.DeleteGuardrailRequest](../operations/deleteguardrailrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[models.DeleteGuardrailResponse](../models/deleteguardrailresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## listKeyAssignments

List all API key guardrail assignments for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | const result = await openRouter.guardrails.listKeyAssignments(); |
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
| 2 | import { guardrailsListKeyAssignments } from "@openrouter/sdk/funcs/guardrailsListKeyAssignments.js"; |
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
| 14 | const res = await guardrailsListKeyAssignments(openRouter); |
| 15 | if (res.ok) { |
| 16 | const { value: result } = res; |
| 17 | for await (const page of result) { |
| 18 | console.log(page); |
| 19 | } |
| 20 | } else { |
| 21 | console.log("guardrailsListKeyAssignments failed:", res.error); |
| 22 | } |
| 23 | } |
| 24 |  |
| 25 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.ListKeyAssignmentsRequest](../operations/listkeyassignmentsrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.ListKeyAssignmentsResponse](../operations/listkeyassignmentsresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## listMemberAssignments

List all organization member guardrail assignments for the authenticated user. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | const result = await openRouter.guardrails.listMemberAssignments(); |
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
| 2 | import { guardrailsListMemberAssignments } from "@openrouter/sdk/funcs/guardrailsListMemberAssignments.js"; |
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
| 14 | const res = await guardrailsListMemberAssignments(openRouter); |
| 15 | if (res.ok) { |
| 16 | const { value: result } = res; |
| 17 | for await (const page of result) { |
| 18 | console.log(page); |
| 19 | } |
| 20 | } else { |
| 21 | console.log("guardrailsListMemberAssignments failed:", res.error); |
| 22 | } |
| 23 | } |
| 24 |  |
| 25 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.ListMemberAssignmentsRequest](../operations/listmemberassignmentsrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.ListMemberAssignmentsResponse](../operations/listmemberassignmentsresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## listGuardrailKeyAssignments

List all API key assignments for a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | const result = await openRouter.guardrails.listGuardrailKeyAssignments({ |
| 12 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 13 | }); |
| 14 |  |
| 15 | for await (const page of result) { |
| 16 | console.log(page); |
| 17 | } |
| 18 | } |
| 19 |  |
| 20 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { guardrailsListGuardrailKeyAssignments } from "@openrouter/sdk/funcs/guardrailsListGuardrailKeyAssignments.js"; |
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
| 14 | const res = await guardrailsListGuardrailKeyAssignments(openRouter, { |
| 15 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 16 | }); |
| 17 | if (res.ok) { |
| 18 | const { value: result } = res; |
| 19 | for await (const page of result) { |
| 20 | console.log(page); |
| 21 | } |
| 22 | } else { |
| 23 | console.log("guardrailsListGuardrailKeyAssignments failed:", res.error); |
| 24 | } |
| 25 | } |
| 26 |  |
| 27 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.ListGuardrailKeyAssignmentsRequest](../operations/listguardrailkeyassignmentsrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.ListGuardrailKeyAssignmentsResponse](../operations/listguardrailkeyassignmentsresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## bulkAssignKeys

Assign multiple API keys to a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | const result = await openRouter.guardrails.bulkAssignKeys({ |
| 12 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 13 | bulkAssignKeysRequest: { |
| 14 | keyHashes: [ |
| 15 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 16 | ], |
| 17 | }, |
| 18 | }); |
| 19 |  |
| 20 | console.log(result); |
| 21 | } |
| 22 |  |
| 23 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { guardrailsBulkAssignKeys } from "@openrouter/sdk/funcs/guardrailsBulkAssignKeys.js"; |
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
| 14 | const res = await guardrailsBulkAssignKeys(openRouter, { |
| 15 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 16 | bulkAssignKeysRequest: { |
| 17 | keyHashes: [ |
| 18 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 19 | ], |
| 20 | }, |
| 21 | }); |
| 22 | if (res.ok) { |
| 23 | const { value: result } = res; |
| 24 | console.log(result); |
| 25 | } else { |
| 26 | console.log("guardrailsBulkAssignKeys failed:", res.error); |
| 27 | } |
| 28 | } |
| 29 |  |
| 30 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.BulkAssignKeysToGuardrailRequest](../operations/bulkassignkeystoguardrailrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[models.BulkAssignKeysResponse](../models/bulkassignkeysresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## listGuardrailMemberAssignments

List all organization member assignments for a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | const result = await openRouter.guardrails.listGuardrailMemberAssignments({ |
| 12 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 13 | }); |
| 14 |  |
| 15 | for await (const page of result) { |
| 16 | console.log(page); |
| 17 | } |
| 18 | } |
| 19 |  |
| 20 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { guardrailsListGuardrailMemberAssignments } from "@openrouter/sdk/funcs/guardrailsListGuardrailMemberAssignments.js"; |
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
| 14 | const res = await guardrailsListGuardrailMemberAssignments(openRouter, { |
| 15 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 16 | }); |
| 17 | if (res.ok) { |
| 18 | const { value: result } = res; |
| 19 | for await (const page of result) { |
| 20 | console.log(page); |
| 21 | } |
| 22 | } else { |
| 23 | console.log("guardrailsListGuardrailMemberAssignments failed:", res.error); |
| 24 | } |
| 25 | } |
| 26 |  |
| 27 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.ListGuardrailMemberAssignmentsRequest](../operations/listguardrailmemberassignmentsrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.ListGuardrailMemberAssignmentsResponse](../operations/listguardrailmemberassignmentsresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## bulkAssignMembers

Assign multiple organization members to a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | const result = await openRouter.guardrails.bulkAssignMembers({ |
| 12 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 13 | bulkAssignMembersRequest: { |
| 14 | memberUserIds: [ |
| 15 | "user_abc123", |
| 16 | "user_def456", |
| 17 | ], |
| 18 | }, |
| 19 | }); |
| 20 |  |
| 21 | console.log(result); |
| 22 | } |
| 23 |  |
| 24 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { guardrailsBulkAssignMembers } from "@openrouter/sdk/funcs/guardrailsBulkAssignMembers.js"; |
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
| 14 | const res = await guardrailsBulkAssignMembers(openRouter, { |
| 15 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 16 | bulkAssignMembersRequest: { |
| 17 | memberUserIds: [ |
| 18 | "user_abc123", |
| 19 | "user_def456", |
| 20 | ], |
| 21 | }, |
| 22 | }); |
| 23 | if (res.ok) { |
| 24 | const { value: result } = res; |
| 25 | console.log(result); |
| 26 | } else { |
| 27 | console.log("guardrailsBulkAssignMembers failed:", res.error); |
| 28 | } |
| 29 | } |
| 30 |  |
| 31 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.BulkAssignMembersToGuardrailRequest](../operations/bulkassignmemberstoguardrailrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[models.BulkAssignMembersResponse](../models/bulkassignmembersresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## bulkUnassignKeys

Unassign multiple API keys from a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | const result = await openRouter.guardrails.bulkUnassignKeys({ |
| 12 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 13 | bulkUnassignKeysRequest: { |
| 14 | keyHashes: [ |
| 15 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 16 | ], |
| 17 | }, |
| 18 | }); |
| 19 |  |
| 20 | console.log(result); |
| 21 | } |
| 22 |  |
| 23 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { guardrailsBulkUnassignKeys } from "@openrouter/sdk/funcs/guardrailsBulkUnassignKeys.js"; |
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
| 14 | const res = await guardrailsBulkUnassignKeys(openRouter, { |
| 15 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 16 | bulkUnassignKeysRequest: { |
| 17 | keyHashes: [ |
| 18 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 19 | ], |
| 20 | }, |
| 21 | }); |
| 22 | if (res.ok) { |
| 23 | const { value: result } = res; |
| 24 | console.log(result); |
| 25 | } else { |
| 26 | console.log("guardrailsBulkUnassignKeys failed:", res.error); |
| 27 | } |
| 28 | } |
| 29 |  |
| 30 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.BulkUnassignKeysFromGuardrailRequest](../operations/bulkunassignkeysfromguardrailrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[models.BulkUnassignKeysResponse](../models/bulkunassignkeysresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## bulkUnassignMembers

Unassign multiple organization members from a specific guardrail. [Management key](../../../../guides/overview/auth/management-api-keys/index.md) required.

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
| 11 | const result = await openRouter.guardrails.bulkUnassignMembers({ |
| 12 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 13 | bulkUnassignMembersRequest: { |
| 14 | memberUserIds: [ |
| 15 | "user_abc123", |
| 16 | "user_def456", |
| 17 | ], |
| 18 | }, |
| 19 | }); |
| 20 |  |
| 21 | console.log(result); |
| 22 | } |
| 23 |  |
| 24 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { guardrailsBulkUnassignMembers } from "@openrouter/sdk/funcs/guardrailsBulkUnassignMembers.js"; |
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
| 14 | const res = await guardrailsBulkUnassignMembers(openRouter, { |
| 15 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 16 | bulkUnassignMembersRequest: { |
| 17 | memberUserIds: [ |
| 18 | "user_abc123", |
| 19 | "user_def456", |
| 20 | ], |
| 21 | }, |
| 22 | }); |
| 23 | if (res.ok) { |
| 24 | const { value: result } = res; |
| 25 | console.log(result); |
| 26 | } else { |
| 27 | console.log("guardrailsBulkUnassignMembers failed:", res.error); |
| 28 | } |
| 29 | } |
| 30 |  |
| 31 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.BulkUnassignMembersFromGuardrailRequest](../operations/bulkunassignmembersfromguardrailrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[models.BulkUnassignMembersResponse](../models/bulkunassignmembersresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
