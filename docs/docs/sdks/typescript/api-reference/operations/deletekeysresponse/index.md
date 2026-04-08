---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/deletekeysresponse"
title: "DeleteKeysResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:02.875559+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

DeleteKeysResponse - TypeScript SDK

DeleteKeysResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

API key deleted successfully

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { DeleteKeysResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: DeleteKeysResponse = { |
| 4 | deleted: true, |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `deleted` | *true* | ✔️ | Confirmation that the API key was deleted | true |
