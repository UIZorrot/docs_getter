---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/datacollection"
title: "DataCollection Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:19.823572+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

DataCollection - TypeScript SDK

DataCollection type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Data collection setting. If no available model provider meets the requirement, your request will return an error.

- allow: (default) allow providers which store user data non-transiently and may train on it
- deny: use only providers which do not collect user data.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { DataCollection } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: DataCollection = "allow"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "deny" | "allow" | Unrecognized<string> |
```
