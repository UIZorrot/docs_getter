---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/effort"
title: "Effort Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:19.747995+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

Effort - TypeScript SDK

Effort type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Constrains effort on reasoning for reasoning models

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Effort } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: Effort = "medium"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "xhigh" | "high" | "medium" | "low" | "minimal" | "none" | Unrecognized<string> |
```
