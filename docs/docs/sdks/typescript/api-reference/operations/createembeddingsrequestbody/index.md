---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createembeddingsrequestbody"
title: "CreateEmbeddingsRequestBody Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.146887+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateEmbeddingsRequestBody - TypeScript SDK

CreateEmbeddingsRequestBody type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Embeddings request input

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateEmbeddingsRequestBody } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateEmbeddingsRequestBody = { |
| 4 | input: "The quick brown fox jumps over the lazy dog", |
| 5 | model: "openai/text-embedding-3-small", |
| 6 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `input` | *operations.InputUnion* | ✔️ | Text, token, or multimodal input(s) to embed | The quick brown fox jumps over the lazy dog |
| `model` | *string* | ✔️ | The model to use for embeddings | openai/text-embedding-3-small |
| `encodingFormat` | [operations.EncodingFormat](../encodingformat/index.md) | ➖ | The format of the output embeddings | float |
| `dimensions` | *number* | ➖ | The number of dimensions for the output embeddings | 1536 |
| `user` | *string* | ➖ | A unique identifier for the end-user | user-1234 |
| `provider` | [models.ProviderPreferences](../../models/providerpreferences/index.md) | ➖ | N/A | `{"allow_fallbacks": true}` |
| `inputType` | *string* | ➖ | The type of input (e.g. search\_query, search\_document) | search\_query |
