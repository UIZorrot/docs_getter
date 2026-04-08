---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/rerank"
title: "Rerank | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:47.598699+00:00"
---
[TypeScript SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Rerank - TypeScript SDK

Rerank method reference

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

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
| 11 | const result = await openRouter.rerank.rerank({ |
| 12 | requestBody: { |
| 13 | model: "cohere/rerank-v3.5", |
| 14 | query: "What is the capital of France?", |
| 15 | documents: [ |
| 16 | "Paris is the capital of France.", |
| 17 | "Berlin is the capital of Germany.", |
| 18 | "Madrid is the capital of Spain.", |
| 19 | ], |
| 20 | }, |
| 21 | }); |
| 22 |  |
| 23 | console.log(result); |
| 24 | } |
| 25 |  |
| 26 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { rerankRerank } from "@openrouter/sdk/funcs/rerankRerank.js"; |
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
| 14 | const res = await rerankRerank(openRouter, { |
| 15 | requestBody: { |
| 16 | model: "cohere/rerank-v3.5", |
| 17 | query: "What is the capital of France?", |
| 18 | documents: [ |
| 19 | "Paris is the capital of France.", |
| 20 | "Berlin is the capital of Germany.", |
| 21 | "Madrid is the capital of Spain.", |
| 22 | ], |
| 23 | }, |
| 24 | }); |
| 25 | if (res.ok) { |
| 26 | const { value: result } = res; |
| 27 | console.log(result); |
| 28 | } else { |
| 29 | console.log("rerankRerank failed:", res.error); |
| 30 | } |
| 31 | } |
| 32 |  |
| 33 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.CreateRerankRequest](../operations/creatererankrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.CreateRerankResponse](../operations/creatererankresponse/index.md)>**

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
