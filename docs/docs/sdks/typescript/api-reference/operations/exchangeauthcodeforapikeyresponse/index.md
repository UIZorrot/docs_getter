---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/exchangeauthcodeforapikeyresponse"
title: "ExchangeAuthCodeForAPIKeyResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.983388+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ExchangeAuthCodeForAPIKeyResponse - TypeScript SDK

ExchangeAuthCodeForAPIKeyResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Successfully exchanged code for an API key

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ExchangeAuthCodeForAPIKeyResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ExchangeAuthCodeForAPIKeyResponse = { |
| 4 | key: |
| 5 | "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", |
| 6 | userId: "user_2yOPcMpKoQhcd4bVgSMlELRaIah", |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `key` | *string* | ✔️ | The API key to use for OpenRouter requests | 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 |
| `userId` | *string* | ✔️ | User ID associated with the API key | user\_2yOPcMpKoQhcd4bVgSMlELRaIah |
