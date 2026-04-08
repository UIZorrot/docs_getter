---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/chat"
title: "Chat | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:46.165841+00:00"
---
[TypeScript SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Chat - TypeScript SDK

Chat method reference

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Overview

### Available Operations

- [send](#send) - Create a chat completion

## send

Sends a request for a model response for the given chat conversation. Supports both streaming and non-streaming modes.

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
| 11 | const result = await openRouter.chat.send({ |
| 12 | chatRequest: { |
| 13 | messages: [ |
| 14 | { |
| 15 | role: "system", |
| 16 | content: "You are a helpful assistant.", |
| 17 | }, |
| 18 | { |
| 19 | role: "user", |
| 20 | content: "What is the capital of France?", |
| 21 | }, |
| 22 | ], |
| 23 | model: "openai/gpt-4", |
| 24 | maxTokens: 150, |
| 25 | temperature: 0.7, |
| 26 | }, |
| 27 | }); |
| 28 |  |
| 29 | console.log(result); |
| 30 | } |
| 31 |  |
| 32 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { chatSend } from "@openrouter/sdk/funcs/chatSend.js"; |
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
| 14 | const res = await chatSend(openRouter, { |
| 15 | chatRequest: { |
| 16 | messages: [ |
| 17 | { |
| 18 | role: "system", |
| 19 | content: "You are a helpful assistant.", |
| 20 | }, |
| 21 | { |
| 22 | role: "user", |
| 23 | content: "What is the capital of France?", |
| 24 | }, |
| 25 | ], |
| 26 | model: "openai/gpt-4", |
| 27 | maxTokens: 150, |
| 28 | temperature: 0.7, |
| 29 | }, |
| 30 | }); |
| 31 | if (res.ok) { |
| 32 | const { value: result } = res; |
| 33 | console.log(result); |
| 34 | } else { |
| 35 | console.log("chatSend failed:", res.error); |
| 36 | } |
| 37 | } |
| 38 |  |
| 39 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.SendChatCompletionRequestRequest](../operations/sendchatcompletionrequestrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.SendChatCompletionRequestResponse](../operations/sendchatcompletionrequestresponse/index.md)>**

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
