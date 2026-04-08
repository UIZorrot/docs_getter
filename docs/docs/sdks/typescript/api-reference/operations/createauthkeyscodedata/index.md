---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createauthkeyscodedata"
title: "CreateAuthKeysCodeData Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.545326+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateAuthKeysCodeData - TypeScript SDK

CreateAuthKeysCodeData type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Auth code data

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateAuthKeysCodeData } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateAuthKeysCodeData = { |
| 4 | id: "auth_code_xyz789", |
| 5 | appId: 12345, |
| 6 | createdAt: "2025-08-24T10:30:00Z", |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *string* | ✔️ | The authorization code ID to use in the exchange request | auth\_code\_xyz789 |
| `appId` | *number* | ✔️ | The application ID associated with this auth code | 12345 |
| `createdAt` | *string* | ✔️ | ISO 8601 timestamp of when the auth code was created | 2025-08-24T10:30:00Z |
