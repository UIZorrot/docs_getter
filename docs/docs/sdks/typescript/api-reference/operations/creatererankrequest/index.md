---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/creatererankrequest"
title: "CreateRerankRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:06.521157+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

CreateRerankRequest - TypeScript SDK

CreateRerankRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { CreateRerankRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: CreateRerankRequest = { |
| 4 | requestBody: { |
| 5 | model: "cohere/rerank-v3.5", |
| 6 | query: "What is the capital of France?", |
| 7 | documents: [ |
| 8 | "Paris is the capital of France.", |
| 9 | "Berlin is the capital of Germany.", |
| 10 | ], |
| 11 | }, |
| 12 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `requestBody` | [operations.CreateRerankRequestBody](../creatererankrequestbody/index.md) | ✔️ | N/A | `{"model": "cohere/rerank-v3.5","query": "What is the capital of France?","documents": ["Paris is the capital of France.","Berlin is the capital of Germany."],"top_n": 3}` |
