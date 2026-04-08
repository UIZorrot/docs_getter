---
source_url: "https://openrouter.ai/docs/guides/routing/model-variants/extended"
title: "Extended Variant | Extended Context Windows | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:41.683445+00:00"
---
[Models & Routing](../../model-fallbacks/index.md)[Model Variants](../free/index.md)

# Extended Variant

Extended context windows with :extended

The `:extended` variant provides access to model versions with extended context windows.

## Usage

Append `:extended` to any model ID:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "anthropic/claude-sonnet-4.5:extended" |
| 3 | } |
```

## Details

Extended variants offer larger context windows than the standard model versions, allowing you to process longer inputs and maintain more conversation history.
