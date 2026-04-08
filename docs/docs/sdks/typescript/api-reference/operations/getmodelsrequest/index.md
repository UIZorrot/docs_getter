---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/getmodelsrequest"
title: "GetModelsRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:05.922168+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

GetModelsRequest - TypeScript SDK

GetModelsRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { GetModelsRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: GetModelsRequest = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `category` | [operations.Category](../category/index.md) | ➖ | Filter models by use case category | programming |
| `supportedParameters` | *string* | ➖ | Filter models by supported parameter (comma-separated) | temperature |
| `outputModalities` | *string* | ➖ | Filter models by output modality. Accepts a comma-separated list of modalities (text, image, audio, embeddings) or “all” to include all models. Defaults to “text”. | text |
