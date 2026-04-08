---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createauthkeyscoderequest"
title: "CreateAuthKeysCodeRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.887016+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateAuthKeysCodeRequest - TypeScript SDK

CreateAuthKeysCodeRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateAuthKeysCodeRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateAuthKeysCodeRequest = { |
| 4 | requestBody: { |
| 5 | callbackUrl: "https://myapp.com/auth/callback", |
| 6 | }, |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `requestBody` | [operations.CreateAuthKeysCodeRequestBody](../createauthkeyscoderequestbody/index.md) | ✔️ | N/A | `{"callback_url": "https://myapp.com/auth/callback","code_challenge": "E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM","code_challenge_method": "S256","limit": 100}` |
