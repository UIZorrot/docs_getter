---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/bulkunassignkeysrequest"
title: "BulkUnassignKeysRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.690983+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

BulkUnassignKeysRequest - TypeScript SDK

BulkUnassignKeysRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { BulkUnassignKeysRequest } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: BulkUnassignKeysRequest = { |
| 4 | keyHashes: [ |
| 5 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 6 | ], |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `keyHashes` | *string*[] | ✔️ | Array of API key hashes to unassign from the guardrail | [ “c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93” ] |
