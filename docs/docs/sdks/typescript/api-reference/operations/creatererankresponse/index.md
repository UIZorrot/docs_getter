---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/creatererankresponse"
title: "CreateRerankResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.460454+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateRerankResponse - TypeScript SDK

CreateRerankResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Supported Types

### `operations.CreateRerankResponseBody`

```
|  |  |
| --- | --- |
| 1 | const value: operations.CreateRerankResponseBody = { |
| 2 | model: "cohere/rerank-v3.5", |
| 3 | results: [ |
| 4 | { |
| 5 | index: 0, |
| 6 | relevanceScore: 0.98, |
| 7 | document: { |
| 8 | text: "Paris is the capital of France.", |
| 9 | }, |
| 10 | }, |
| 11 | ], |
| 12 | }; |
```

### `string`

```
|  |  |
| --- | --- |
| 1 | const value: string = "<value>"; |
```
