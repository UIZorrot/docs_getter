---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/maxprice"
title: "MaxPrice Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:20.132605+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

MaxPrice - TypeScript SDK

MaxPrice type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

The object specifying the maximum price you want to pay for this request. USD price per million tokens, for prompt and completion.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { MaxPrice } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: MaxPrice = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `prompt` | *string* | ➖ | Price per million prompt tokens | 1000 |
| `completion` | *string* | ➖ | N/A | 1000 |
| `image` | *string* | ➖ | N/A | 1000 |
| `audio` | *string* | ➖ | N/A | 1000 |
| `request` | *string* | ➖ | N/A | 1000 |
