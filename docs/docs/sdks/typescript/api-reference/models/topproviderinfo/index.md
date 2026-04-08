---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/topproviderinfo"
title: "TopProviderInfo Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:18.700763+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

TopProviderInfo - TypeScript SDK

TopProviderInfo type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Information about the top provider for this model

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { TopProviderInfo } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: TopProviderInfo = { |
| 4 | isModerated: true, |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `contextLength` | *number* | ➖ | Context length from the top provider | 8192 |
| `maxCompletionTokens` | *number* | ➖ | Maximum completion tokens from the top provider | 4096 |
| `isModerated` | *boolean* | ✔️ | Whether the top provider moderates content | true |
