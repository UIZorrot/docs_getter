---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/createembeddingsrequest"
title: "CreateEmbeddingsRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.407270+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateEmbeddingsRequest - TypeScript SDK

CreateEmbeddingsRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateEmbeddingsRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateEmbeddingsRequest = { |
| 4 | requestBody: { |
| 5 | input: "The quick brown fox jumps over the lazy dog", |
| 6 | model: "openai/text-embedding-3-small", |
| 7 | }, |
| 8 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `requestBody` | [operations.CreateEmbeddingsRequestBody](../createembeddingsrequestbody/index.md) | ✔️ | N/A | `{"model": "openai/text-embedding-3-small","input": "The quick brown fox jumps over the lazy dog","dimensions": 1536}` |
