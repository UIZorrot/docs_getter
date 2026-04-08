---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/creatererankrequestbody"
title: "CreateRerankRequestBody Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.213053+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateRerankRequestBody - TypeScript SDK

CreateRerankRequestBody type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Rerank request input

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateRerankRequestBody } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateRerankRequestBody = { |
| 4 | model: "cohere/rerank-v3.5", |
| 5 | query: "What is the capital of France?", |
| 6 | documents: [ |
| 7 | "Paris is the capital of France.", |
| 8 | "Berlin is the capital of Germany.", |
| 9 | ], |
| 10 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `model` | *string* | ✔️ | The rerank model to use | cohere/rerank-v3.5 |
| `query` | *string* | ✔️ | The search query to rerank documents against | What is the capital of France? |
| `documents` | *string*[] | ✔️ | The list of documents to rerank | [ “Paris is the capital of France.”, “Berlin is the capital of Germany.” ] |
| `topN` | *number* | ➖ | Number of most relevant documents to return | 3 |
| `provider` | [models.ProviderPreferences](../../models/providerpreferences/index.md) | ➖ | N/A | `{"allow_fallbacks": true}` |
