---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/exchangeauthcodeforapikeyrequest"
title: "ExchangeAuthCodeForAPIKeyRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.638241+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ExchangeAuthCodeForAPIKeyRequest - TypeScript SDK

ExchangeAuthCodeForAPIKeyRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ExchangeAuthCodeForAPIKeyRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ExchangeAuthCodeForAPIKeyRequest = { |
| 4 | requestBody: { |
| 5 | code: "auth_code_abc123def456", |
| 6 | }, |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `requestBody` | [operations.ExchangeAuthCodeForAPIKeyRequestBody](../exchangeauthcodeforapikeyrequestbody/index.md) | ✔️ | N/A | `{"code": "auth_code_abc123def456","code_verifier": "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk","code_challenge_method": "S256"}` |
