---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/inputmodality"
title: "InputModality Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:20.594534+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

InputModality - TypeScript SDK

InputModality type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { InputModality } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: InputModality = "text"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "text" | "image" | "file" | "audio" | "video" | Unrecognized<string> |
```
