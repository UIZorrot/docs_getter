---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/pricing"
title: "Pricing Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.919228+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

Pricing - TypeScript SDK

Pricing type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Pricing } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: Pricing = { |
| 4 | prompt: "1000", |
| 5 | completion: "1000", |
| 6 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `prompt` | *string* | ✔️ | N/A | 1000 |
| `completion` | *string* | ✔️ | N/A | 1000 |
| `request` | *string* | ➖ | N/A | 1000 |
| `image` | *string* | ➖ | N/A | 1000 |
| `imageToken` | *string* | ➖ | N/A | 1000 |
| `imageOutput` | *string* | ➖ | N/A | 1000 |
| `audio` | *string* | ➖ | N/A | 1000 |
| `audioOutput` | *string* | ➖ | N/A | 1000 |
| `inputAudioCache` | *string* | ➖ | N/A | 1000 |
| `webSearch` | *string* | ➖ | N/A | 1000 |
| `internalReasoning` | *string* | ➖ | N/A | 1000 |
| `inputCacheRead` | *string* | ➖ | N/A | 1000 |
| `inputCacheWrite` | *string* | ➖ | N/A | 1000 |
| `discount` | *number* | ➖ | N/A |  |
