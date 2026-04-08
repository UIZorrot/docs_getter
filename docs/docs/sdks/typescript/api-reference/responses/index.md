---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/responses"
title: "Beta.Responses | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:47.817739+00:00"
---
[TypeScript SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Beta.Responses - TypeScript SDK

Beta.Responses method reference

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Overview

beta.responses endpoints

### Available Operations

- [send](#send) - Create a response

## send

Creates a streaming or non-streaming response using OpenResponses API format

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
| 11 | const result = await openRouter.beta.responses.send({ |
| 12 | responsesRequest: { |
| 13 | input: "Tell me a joke", |
| 14 | model: "openai/gpt-4o", |
| 15 | }, |
| 16 | }); |
| 17 |  |
| 18 | console.log(result); |
| 19 | } |
| 20 |  |
| 21 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { betaResponsesSend } from "@openrouter/sdk/funcs/betaResponsesSend.js"; |
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
| 14 | const res = await betaResponsesSend(openRouter, { |
| 15 | responsesRequest: { |
| 16 | input: "Tell me a joke", |
| 17 | model: "openai/gpt-4o", |
| 18 | }, |
| 19 | }); |
| 20 | if (res.ok) { |
| 21 | const { value: result } = res; |
| 22 | console.log(result); |
| 23 | } else { |
| 24 | console.log("betaResponsesSend failed:", res.error); |
| 25 | } |
| 26 | } |
| 27 |  |
| 28 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.CreateResponsesRequest](../operations/createresponsesrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.CreateResponsesResponse](../operations/createresponsesresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.PaymentRequiredResponseError | 402 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.RequestTimeoutResponseError | 408 | application/json |
| errors.PayloadTooLargeResponseError | 413 | application/json |
| errors.UnprocessableEntityResponseError | 422 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.BadGatewayResponseError | 502 | application/json |
| errors.ServiceUnavailableResponseError | 503 | application/json |
| errors.EdgeNetworkTimeoutResponseError | 524 | application/json |
| errors.ProviderOverloadedResponseError | 529 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
