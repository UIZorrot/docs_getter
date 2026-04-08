---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/responseincludesenum"
title: "ResponseIncludesEnum Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:19.383339+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ResponseIncludesEnum - TypeScript SDK

ResponseIncludesEnum type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ResponseIncludesEnum } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ResponseIncludesEnum = "file_search_call.results"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "file_search_call.results" | "message.input_image.image_url" | "computer_call_output.output.image_url" | "reasoning.encrypted_content" | "code_interpreter_call.outputs" | Unrecognized<string> |
```
