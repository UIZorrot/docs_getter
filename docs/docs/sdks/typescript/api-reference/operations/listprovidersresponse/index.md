---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listprovidersresponse"
title: "ListProvidersResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:07.134219+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListProvidersResponse - TypeScript SDK

ListProvidersResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Returns a list of providers

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListProvidersResponse } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListProvidersResponse = { |
| 4 | data: [ |
| 5 | { |
| 6 | name: "OpenAI", |
| 7 | slug: "openai", |
| 8 | privacyPolicyUrl: "https://openai.com/privacy", |
| 9 | }, |
| 10 | ], |
| 11 | }; |
```

## Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | [operations.ListProvidersData](../listprovidersdata/index.md)[] | ✔️ | N/A |
