---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createresponsesresponse"
title: "CreateResponsesResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:07.091785+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateResponsesResponse - TypeScript SDK

CreateResponsesResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Supported Types

### `models.OpenResponsesResult`

```
|  |  |
| --- | --- |
| 1 | const value: models.OpenResponsesResult = { |
| 2 | id: "resp-abc123", |
| 3 | object: "response", |
| 4 | createdAt: 1704067200, |
| 5 | model: "gpt-4", |
| 6 | status: "completed", |
| 7 | completedAt: 311936, |
| 8 | output: [ |
| 9 | { |
| 10 | type: "message", |
| 11 | status: "completed", |
| 12 | }, |
| 13 | ], |
| 14 | error: null, |
| 15 | incompleteDetails: null, |
| 16 | temperature: 7286.67, |
| 17 | topP: 3737.69, |
| 18 | presencePenalty: 9990.37, |
| 19 | frequencyPenalty: 461.05, |
| 20 | instructions: null, |
| 21 | metadata: null, |
| 22 | tools: [], |
| 23 | toolChoice: "auto", |
| 24 | parallelToolCalls: true, |
| 25 | }; |
```

### `EventStream<operations.CreateResponsesResponseBody>`
