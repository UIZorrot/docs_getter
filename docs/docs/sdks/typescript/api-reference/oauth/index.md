---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/oauth"
title: "OAuth | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:47.719541+00:00"
---
[TypeScript SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

OAuth - TypeScript SDK

OAuth method reference

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Overview

OAuth authentication endpoints

### Available Operations

- [exchangeAuthCodeForAPIKey](#exchangeauthcodeforapikey) - Exchange authorization code for API key
- [createAuthCode](#createauthcode) - Create authorization code

## exchangeAuthCodeForAPIKey

Exchange an authorization code from the PKCE flow for a user-controlled API key

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
| 11 | const result = await openRouter.oAuth.exchangeAuthCodeForAPIKey({ |
| 12 | requestBody: { |
| 13 | code: "auth_code_abc123def456", |
| 14 | codeVerifier: "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk", |
| 15 | codeChallengeMethod: "S256", |
| 16 | }, |
| 17 | }); |
| 18 |  |
| 19 | console.log(result); |
| 20 | } |
| 21 |  |
| 22 | run(); |
```

### Standalone function

The standalone function version of this method:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouterCore } from "@openrouter/sdk/core.js"; |
| 2 | import { oAuthExchangeAuthCodeForAPIKey } from "@openrouter/sdk/funcs/oAuthExchangeAuthCodeForAPIKey.js"; |
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
| 14 | const res = await oAuthExchangeAuthCodeForAPIKey(openRouter, { |
| 15 | requestBody: { |
| 16 | code: "auth_code_abc123def456", |
| 17 | codeVerifier: "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk", |
| 18 | codeChallengeMethod: "S256", |
| 19 | }, |
| 20 | }); |
| 21 | if (res.ok) { |
| 22 | const { value: result } = res; |
| 23 | console.log(result); |
| 24 | } else { |
| 25 | console.log("oAuthExchangeAuthCodeForAPIKey failed:", res.error); |
| 26 | } |
| 27 | } |
| 28 |  |
| 29 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.ExchangeAuthCodeForAPIKeyRequest](../operations/exchangeauthcodeforapikeyrequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.ExchangeAuthCodeForAPIKeyResponse](../operations/exchangeauthcodeforapikeyresponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.ForbiddenResponseError | 403 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |

## createAuthCode

Create an authorization code for the PKCE flow to generate a user-controlled API key

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
| 11 | const result = await openRouter.oAuth.createAuthCode({ |
| 12 | requestBody: { |
| 13 | callbackUrl: "https://myapp.com/auth/callback", |
| 14 | codeChallenge: "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM", |
| 15 | codeChallengeMethod: "S256", |
| 16 | limit: 100, |
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
| 2 | import { oAuthCreateAuthCode } from "@openrouter/sdk/funcs/oAuthCreateAuthCode.js"; |
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
| 14 | const res = await oAuthCreateAuthCode(openRouter, { |
| 15 | requestBody: { |
| 16 | callbackUrl: "https://myapp.com/auth/callback", |
| 17 | codeChallenge: "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM", |
| 18 | codeChallengeMethod: "S256", |
| 19 | limit: 100, |
| 20 | }, |
| 21 | }); |
| 22 | if (res.ok) { |
| 23 | const { value: result } = res; |
| 24 | console.log(result); |
| 25 | } else { |
| 26 | console.log("oAuthCreateAuthCode failed:", res.error); |
| 27 | } |
| 28 | } |
| 29 |  |
| 30 | run(); |
```

### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `request` | [operations.CreateAuthKeysCodeRequest](../operations/createauthkeyscoderequest/index.md) | ✔️ | The request object to use for the request. |
| `options` | RequestOptions | ➖ | Used to set various options for making HTTP requests. |
| `options.fetchOptions` | [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request) | ➖ | Options that are passed to the underlying HTTP request. This can be used to inject extra headers for examples. All `Request` options, except `method` and `body`, are allowed. |
| `options.retries` | [RetryConfig](../lib/retryconfig/index.md) | ➖ | Enables retrying HTTP requests under certain failure conditions. |

### Response

**Promise<[operations.CreateAuthKeysCodeResponse](../operations/createauthkeyscoderesponse/index.md)>**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.ConflictResponseError | 409 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
