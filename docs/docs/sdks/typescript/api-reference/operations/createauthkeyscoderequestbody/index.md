---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createauthkeyscoderequestbody"
title: "CreateAuthKeysCodeRequestBody Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.373118+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateAuthKeysCodeRequestBody - TypeScript SDK

CreateAuthKeysCodeRequestBody type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateAuthKeysCodeRequestBody } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateAuthKeysCodeRequestBody = { |
| 4 | callbackUrl: "https://myapp.com/auth/callback", |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `callbackUrl` | *string* | ✔️ | The callback URL to redirect to after authorization. Note, only https URLs on ports 443 and 3000 are allowed. | [https://myapp.com/auth/callback](https://myapp.com/auth/callback) |
| `codeChallenge` | *string* | ➖ | PKCE code challenge for enhanced security | E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM |
| `codeChallengeMethod` | [operations.CreateAuthKeysCodeCodeChallengeMethod](../createauthkeyscodecodechallengemethod/index.md) | ➖ | The method used to generate the code challenge | S256 |
| `limit` | *number* | ➖ | Credit limit for the API key to be created | 100 |
| `expiresAt` | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | ➖ | Optional expiration time for the API key to be created | 2027-12-31T23:59:59Z |
| `keyLabel` | *string* | ➖ | Optional custom label for the API key. Defaults to the app name if not provided. | My Custom Key |
| `usageLimitType` | [operations.UsageLimitType](../usagelimittype/index.md) | ➖ | Optional credit limit reset interval. When set, the credit limit resets on this interval. | monthly |
