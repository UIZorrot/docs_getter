---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/parameter"
title: "Parameter Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:18.000176+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

Parameter - TypeScript SDK

Parameter type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Parameter } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: Parameter = "temperature"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "temperature" | "top_p" | "top_k" | "min_p" | "top_a" | "frequency_penalty" | "presence_penalty" | "repetition_penalty" | "max_tokens" | "logit_bias" | "logprobs" | "top_logprobs" | "seed" | "response_format" | "structured_outputs" | "stop" | "tools" | "tool_choice" | "parallel_tool_calls" | "include_reasoning" | "reasoning" | "reasoning_effort" | "web_search_options" | "verbosity" | Unrecognized<string> |
```
