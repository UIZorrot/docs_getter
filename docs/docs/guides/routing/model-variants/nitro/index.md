---
source_url: "https://openrouter.ai/docs/guides/routing/model-variants/nitro"
title: "Nitro Variant | High-Speed Inference | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:41.965519+00:00"
---
[Models & Routing](../../model-fallbacks/index.md)[Model Variants](../free/index.md)

# Nitro Variant

High-speed model inference with :nitro

The `:nitro` variant is an alias for sorting providers by throughput. When you use `:nitro`, OpenRouter will prioritize providers with the highest throughput (tokens per second).

## Usage

Append `:nitro` to any model ID:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2:nitro" |
| 3 | } |
```

This is exactly equivalent to setting `provider.sort` to `"throughput"` in your request. For more details on provider sorting, see the [Provider Routing documentation](../../../../features/provider-routing/index.md).
