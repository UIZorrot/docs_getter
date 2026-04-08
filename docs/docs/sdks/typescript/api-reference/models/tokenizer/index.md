---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/tokenizer"
title: "Tokenizer Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:20.044232+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

Tokenizer - TypeScript SDK

Tokenizer type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Tokenizer type used by the model

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Tokenizer } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: Tokenizer = "GPT"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "Router" | "Media" | "Other" | "GPT" | "Claude" | "Gemini" | "Gemma" | "Grok" | "Cohere" | "Nova" | "Qwen" | "Yi" | "DeepSeek" | "Mistral" | "Llama2" | "Llama3" | "Llama4" | "PaLM" | "RWKV" | "Qwen3" | Unrecognized<string> |
```
