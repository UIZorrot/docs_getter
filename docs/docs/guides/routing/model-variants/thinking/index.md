---
source_url: "https://openrouter.ai/docs/guides/routing/model-variants/thinking"
title: "Thinking Variant | Extended Reasoning | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:42.303503+00:00"
---
[Models & Routing](../../model-fallbacks/index.md)[Model Variants](../free/index.md)

# Thinking Variant

Enable extended reasoning with :thinking

The `:thinking` variant enables extended reasoning capabilities for complex problem-solving tasks.

## Usage

Append `:thinking` to any model ID:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "deepseek/deepseek-r1:thinking" |
| 3 | } |
```

## Details

Thinking variants provide access to models with extended reasoning capabilities, allowing for more thorough analysis and step-by-step problem solving. This is particularly useful for complex tasks that benefit from chain-of-thought reasoning.

See also: [Reasoning Tokens](../../../../best-practices/reasoning-tokens/index.md)
