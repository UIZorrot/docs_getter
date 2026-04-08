---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/generations"
title: "Generations | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:46.270478+00:00"
---
[TypeScript SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Generations - TypeScript SDK

Generations method reference

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Overview

Generation history endpoints

### Available Operations

- [getGeneration](#getgeneration) - Get request & usage metadata for a generation

## getGeneration

Get request & usage metadata for a generation

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
| 11 | const result = await openRouter.generations.getGeneration({ |
| 12 | id: "<id>", |
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
| 2 | import { generationsGetGeneration } from "@openrouter/sdk/funcs/generationsGetGeneration.js"; |
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
| 14 | const res = await generationsGetGeneration(openRouter, { |
| 15 | id: "<id>", |
| 16 | }); |
| 17 | if (res.ok) { |
| 18 | const { value: result } = res; |
| 19 | console.log(result); |
| 20 | } else { |
| 21 | console.log("generationsGetGeneration failed:", res.error); |
| 22 | } |
| 23 | } |
| 24 |  |
| 25 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.GetGenerationRequest](../operations/getgenerationrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.GetGenerationResponse](../operations/getgenerationresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.PaymentRequiredResponseError | 402 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.BadGatewayResponseError | 502 | application/json |
| errors.EdgeNetworkTimeoutResponseError | 524 | application/json |
| errors.ProviderOverloadedResponseError | 529 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
