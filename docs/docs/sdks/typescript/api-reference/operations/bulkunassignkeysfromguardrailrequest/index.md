---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/bulkunassignkeysfromguardrailrequest"
title: "BulkUnassignKeysFromGuardrailRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:05.543077+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

BulkUnassignKeysFromGuardrailRequest - TypeScript SDK

BulkUnassignKeysFromGuardrailRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { BulkUnassignKeysFromGuardrailRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: BulkUnassignKeysFromGuardrailRequest = { |
| 4 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 5 | bulkUnassignKeysRequest: { |
| 6 | keyHashes: [ |
| 7 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 8 | ], |
| 9 | }, |
| 10 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `id` | *string* | ✔️ | The unique identifier of the guardrail | 550e8400-e29b-41d4-a716-446655440000 |
| `bulkUnassignKeysRequest` | [models.BulkUnassignKeysRequest](../../models/bulkunassignkeysrequest/index.md) | ✔️ | N/A | `{"key_hashes": ["c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93"]}` |
