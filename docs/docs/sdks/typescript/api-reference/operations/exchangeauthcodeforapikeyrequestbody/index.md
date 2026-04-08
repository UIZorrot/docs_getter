---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/exchangeauthcodeforapikeyrequestbody"
title: "ExchangeAuthCodeForAPIKeyRequestBody Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.268049+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ExchangeAuthCodeForAPIKeyRequestBody - TypeScript SDK

ExchangeAuthCodeForAPIKeyRequestBody type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ExchangeAuthCodeForAPIKeyRequestBody } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ExchangeAuthCodeForAPIKeyRequestBody = { |
| 4 | code: "auth_code_abc123def456", |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `code` | *string* | ✔️ | The authorization code received from the OAuth redirect | auth\_code\_abc123def456 |
| `codeVerifier` | *string* | ➖ | The code verifier if code\_challenge was used in the authorization request | dBjftJeZ4CVP-mB92K27uhbUJU1p1r\_wW1gFWFOEjXk |
| `codeChallengeMethod` | [operations.ExchangeAuthCodeForAPIKeyCodeChallengeMethod](../exchangeauthcodeforapikeycodechallengemethod/index.md) | ➖ | The method used to generate the code challenge | S256 |
