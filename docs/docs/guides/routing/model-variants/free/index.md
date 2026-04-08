---
source_url: "https://openrouter.ai/docs/guides/routing/model-variants/free"
title: "Free Variant | Free Model Access | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:58.518605+00:00"
---
[Models & Routing](../../model-fallbacks/index.md)[Model Variants](index.md)

# Free Variant

Access free models with the :free variant

The `:free` variant allows you to access free versions of models on OpenRouter.

## Usage

Append `:free` to any model ID:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "meta-llama/llama-3.2-3b-instruct:free" |
| 3 | } |
```

## Details

Free variants provide access to models without cost, but may have different rate limits or availability compared to paid versions.

## Related Resources

- [Free Models Router](../../../get-started/free-models-router-playground/index.md) - Learn how to use the Free Models Router in the Chat Playground for zero-cost inference
