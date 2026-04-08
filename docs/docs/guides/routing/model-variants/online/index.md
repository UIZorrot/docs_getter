---
source_url: "https://openrouter.ai/docs/guides/routing/model-variants/online"
title: "Online Variant | Real-Time Web Search | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:42.954595+00:00"
---
[Models & Routing](../../model-fallbacks/index.md)[Model Variants](../free/index.md)

# Online Variant

Real-time web search with :online

##### Deprecated

The `:online` variant is deprecated. Use the [`openrouter:web_search` server tool](../../../features/server-tools/web-search/index.md) instead, which gives the model control over when and how often to search.

If your application already provides the `web_search` tool (e.g. OpenAI’s built-in web search tool type), OpenRouter automatically recognizes it and hoists it to the `openrouter:web_search` server tool. This means you can safely remove the `:online` suffix from any model slug — as long as the application exposes the `web_search` tool, web search functionality will still work as a server tool with any model on OpenRouter.

The `:online` variant enables real-time web search capabilities for any model on OpenRouter.

## Usage

Append `:online` to any model ID:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2:online" |
| 3 | } |
```

This is a shortcut for using the `web` plugin, and is exactly equivalent to:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openrouter/auto", |
| 3 | "plugins": [{ "id": "web" }] |
| 4 | } |
```

## Details

The Online variant incorporates relevant web search results into model responses, providing access to real-time information and current events. This is particularly useful for queries that require up-to-date information beyond the model’s training data.

For the recommended approach, see: [Web Search Server Tool](../../../features/server-tools/web-search/index.md). For legacy plugin details, see: [Web Search Plugin](../../../features/plugins/web-search/index.md).
