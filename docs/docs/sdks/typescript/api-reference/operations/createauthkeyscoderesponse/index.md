---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createauthkeyscoderesponse"
title: "CreateAuthKeysCodeResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.933755+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateAuthKeysCodeResponse - TypeScript SDK

CreateAuthKeysCodeResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Successfully created authorization code

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateAuthKeysCodeResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateAuthKeysCodeResponse = { |
| 4 | data: { |
| 5 | id: "auth_code_xyz789", |
| 6 | appId: 12345, |
| 7 | createdAt: "2025-08-24T10:30:00Z", |
| 8 | }, |
| 9 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [operations.CreateAuthKeysCodeData](../createauthkeyscodedata/index.md) | ✔️ | Auth code data | `{"id": "auth_code_xyz789","app_id": 12345,"created_at": "2025-08-24T10:30:00Z"}` |
