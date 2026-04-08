---
source_url: "https://openrouter.ai/docs/guides/best-practices/prompt-caching"
title: "Prompt Caching | Reduce AI Model Costs with OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:32.634947+00:00"
---
[Best Practices](../latency-and-performance/index.md)

# Prompt Caching

Cache prompt messages

To save on inference costs, you can enable prompt caching on supported providers and models.

Most providers automatically enable prompt caching, but note that some (see Anthropic below) require you to enable it on a per-message basis.

When using caching (whether automatically in supported models, or via the `cache_control` property), OpenRouter uses provider sticky routing to maximize cache hits — see [Provider Sticky Routing](#provider-sticky-routing) below for details.

## Provider Sticky Routing

To maximize cache hit rates, OpenRouter uses **provider sticky routing** to route your subsequent requests to the same provider endpoint after a cached request. This works automatically with both implicit caching (e.g. OpenAI, DeepSeek, Gemini 2.5) and explicit caching (e.g. Anthropic `cache_control` breakpoints).

**How it works:**

- After a request that uses prompt caching, OpenRouter remembers which provider served your request.
- Subsequent requests for the same model are routed to the same provider, keeping your cache warm.
- Sticky routing only activates when the provider’s cache read pricing is cheaper than regular prompt pricing, ensuring you always benefit from cost savings.
- If the sticky provider becomes unavailable, OpenRouter automatically falls back to the next-best provider.
- Sticky routing is not used when you specify a manual [provider order](../../../api-reference/provider-preferences/index.md) via `provider.order` — in that case, your explicit ordering takes priority.

**Sticky routing granularity:**

Sticky routing is tracked at the account level, per model, and per conversation. OpenRouter identifies conversations by hashing the first system (or developer) message and the first non-system message in each request, so requests that share the same opening messages are routed to the same provider. This means different conversations naturally stick to different providers, improving load-balancing and throughput while keeping caches warm within each conversation.

## Inspecting cache usage

To see how much caching saved on each generation, you can:

1. Click the detail button on the [Activity](https://openrouter.ai/activity) page
2. Use the `/api/v1/generation` API, [documented here](../../../api/api-reference/generations/get-generation/index.md)
3. Check the `prompt_tokens_details` object in the [usage response](../../administration/usage-accounting/index.md) included with every API response

The `cache_discount` field in the response body will tell you how much the response saved on cache usage. Some providers, like Anthropic, will have a negative discount on cache writes, but a positive discount (which reduces total cost) on cache reads.

### Usage object fields

The usage object in API responses includes detailed cache metrics in the `prompt_tokens_details` field:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "usage": { |
| 3 | "prompt_tokens": 10339, |
| 4 | "completion_tokens": 60, |
| 5 | "total_tokens": 10399, |
| 6 | "prompt_tokens_details": { |
| 7 | "cached_tokens": 10318, |
| 8 | "cache_write_tokens": 0 |
| 9 | } |
| 10 | } |
| 11 | } |
```

The key fields are:

- `cached_tokens`: Number of tokens read from the cache (cache hit). When this is greater than zero, you’re benefiting from cached content.
- `cache_write_tokens`: Number of tokens written to the cache. This appears on the first request when establishing a new cache entry.

## OpenAI

Caching price changes:

- **Cache writes**: no cost
- **Cache reads**: (depending on the model) charged at 0.25x or 0.50x the price of the original input pricing

[Click here to view OpenAI’s cache pricing per model.](https://platform.openai.com/docs/pricing)

Prompt caching with OpenAI is automated and does not require any additional configuration. There is a minimum prompt size of 1024 tokens.

[Click here to read more about OpenAI prompt caching and its limitation.](https://platform.openai.com/docs/guides/prompt-caching)

## Grok

Caching price changes:

- **Cache writes**: no cost
- **Cache reads**: charged at 0.25x the price of the original input pricing

[Click here to view Grok’s cache pricing per model.](https://docs.x.ai/docs/models)

Prompt caching with Grok is automated and does not require any additional configuration.

## Moonshot AI

Caching price changes:

- **Cache writes**: no cost
- **Cache reads**: charged at 0.25x the price of the original input pricing

Prompt caching with Moonshot AI is automated and does not require any additional configuration.

## Groq

Caching price changes:

- **Cache writes**: no cost
- **Cache reads**: charged at 0.5x the price of the original input pricing

Prompt caching with Groq is automated and does not require any additional configuration. Currently available on Kimi K2 models.

[Click here to view Groq’s documentation.](https://console.groq.com/docs/prompt-caching)

## Anthropic Claude

Caching price changes:

- **Cache writes (5-minute TTL)**: charged at 1.25x the price of the original input pricing
- **Cache writes (1-hour TTL)**: charged at 2x the price of the original input pricing
- **Cache reads**: charged at 0.1x the price of the original input pricing

There are two ways to enable prompt caching with Anthropic:

- **Automatic caching**: Add a single `cache_control` field at the top level of your request. The system automatically applies the cache breakpoint to the last cacheable block and advances it forward as conversations grow. Best for multi-turn conversations.
- **Explicit cache breakpoints**: Place `cache_control` directly on individual content blocks for fine-grained control over exactly what gets cached. There is a limit of four explicit breakpoints. It is recommended to reserve the cache breakpoints for large bodies of text, such as character cards, CSV data, RAG data, book chapters, etc.

##### 

**Automatic caching** (top-level `cache_control`) is only supported when requests are routed to the **Anthropic** provider directly. Amazon Bedrock and Google Vertex AI currently do not support top-level `cache_control` — when it is present, OpenRouter will only route to the Anthropic provider and exclude Bedrock and Vertex endpoints. Explicit per-block `cache_control` breakpoints work across all Anthropic-compatible providers including Bedrock and Vertex.

By default, the cache expires after 5 minutes, but you can extend this to 1 hour by specifying `"ttl": "1h"` in the `cache_control` object.

[Click here to read more about Anthropic prompt caching and its limitation.](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)

### Supported models

The following Claude models support prompt caching (both automatic and explicit):

- Claude Opus 4.6
- Claude Opus 4.5
- Claude Opus 4.1
- Claude Opus 4
- Claude Sonnet 4.6
- Claude Sonnet 4.5
- Claude Sonnet 4
- Claude Sonnet 3.7 (deprecated)
- Claude Haiku 4.5
- Claude Haiku 3.5

### Minimum token requirements

Each model has a minimum cacheable prompt length:

- **4096 tokens**: Claude Opus 4.6, Claude Opus 4.5, Claude Haiku 4.5
- **2048 tokens**: Claude Sonnet 4.6, Claude Haiku 3.5
- **1024 tokens**: Claude Sonnet 4.5, Claude Opus 4.1, Claude Opus 4, Claude Sonnet 4, Claude Sonnet 3.7

Prompts shorter than these minimums will not be cached.

### Cache TTL Options

OpenRouter supports two cache TTL values for Anthropic:

- **5 minutes** (default): `"cache_control": { "type": "ephemeral" }`
- **1 hour**: `"cache_control": { "type": "ephemeral", "ttl": "1h" }`

The 1-hour TTL is useful for longer sessions where you want to maintain cached content across multiple requests without incurring repeated cache write costs. The 1-hour TTL costs more for cache writes (2x base input price vs 1.25x for 5-minute TTL) but can save money over extended sessions by avoiding repeated cache writes. The 1-hour TTL for explicit cache breakpoints is supported across all Claude model providers (Anthropic, Amazon Bedrock, and Google Vertex AI).

### Examples

#### Automatic caching (recommended for multi-turn conversations)

With automatic caching, add `cache_control` at the top level of the request. The system automatically caches all content up to the last cacheable block:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "anthropic/claude-sonnet-4.6", |
| 3 | "cache_control": { "type": "ephemeral" }, |
| 4 | "messages": [ |
| 5 | { |
| 6 | "role": "system", |
| 7 | "content": "You are a historian studying the fall of the Roman Empire. You know the following book very well: HUGE TEXT BODY" |
| 8 | }, |
| 9 | { |
| 10 | "role": "user", |
| 11 | "content": "What triggered the collapse?" |
| 12 | } |
| 13 | ] |
| 14 | } |
```

As the conversation grows, the cache breakpoint automatically advances to cover the growing message history.

Automatic caching with 1-hour TTL:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "anthropic/claude-sonnet-4.6", |
| 3 | "cache_control": { "type": "ephemeral", "ttl": "1h" }, |
| 4 | "messages": [ |
| 5 | { |
| 6 | "role": "system", |
| 7 | "content": "You are a helpful assistant." |
| 8 | }, |
| 9 | { |
| 10 | "role": "user", |
| 11 | "content": "What is the meaning of life?" |
| 12 | } |
| 13 | ] |
| 14 | } |
```

#### Explicit cache breakpoints (fine-grained control)

System message caching example (default 5-minute TTL):

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "messages": [ |
| 3 | { |
| 4 | "role": "system", |
| 5 | "content": [ |
| 6 | { |
| 7 | "type": "text", |
| 8 | "text": "You are a historian studying the fall of the Roman Empire. You know the following book very well:" |
| 9 | }, |
| 10 | { |
| 11 | "type": "text", |
| 12 | "text": "HUGE TEXT BODY", |
| 13 | "cache_control": { |
| 14 | "type": "ephemeral" |
| 15 | } |
| 16 | } |
| 17 | ] |
| 18 | }, |
| 19 | { |
| 20 | "role": "user", |
| 21 | "content": [ |
| 22 | { |
| 23 | "type": "text", |
| 24 | "text": "What triggered the collapse?" |
| 25 | } |
| 26 | ] |
| 27 | } |
| 28 | ] |
| 29 | } |
```

User message caching example with 1-hour TTL:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "messages": [ |
| 3 | { |
| 4 | "role": "user", |
| 5 | "content": [ |
| 6 | { |
| 7 | "type": "text", |
| 8 | "text": "Given the book below:" |
| 9 | }, |
| 10 | { |
| 11 | "type": "text", |
| 12 | "text": "HUGE TEXT BODY", |
| 13 | "cache_control": { |
| 14 | "type": "ephemeral", |
| 15 | "ttl": "1h" |
| 16 | } |
| 17 | }, |
| 18 | { |
| 19 | "type": "text", |
| 20 | "text": "Name all the characters in the above book" |
| 21 | } |
| 22 | ] |
| 23 | } |
| 24 | ] |
| 25 | } |
```

## DeepSeek

Caching price changes:

- **Cache writes**: charged at the same price as the original input pricing
- **Cache reads**: charged at 0.1x the price of the original input pricing

Prompt caching with DeepSeek is automated and does not require any additional configuration.

## Google Gemini

### Implicit Caching

Gemini 2.5 Pro and 2.5 Flash models now support **implicit caching**, providing automatic caching functionality similar to OpenAI’s automatic caching. Implicit caching works seamlessly — no manual setup or additional `cache_control` breakpoints required.

Pricing Changes:

- No cache write or storage costs.
- Cached tokens are charged at 0.25x the original input token cost.

Note that the TTL is on average 3-5 minutes, but will vary. There is a minimum of 1028 tokens for Gemini 2.5 Flash, and 2048 tokens for Gemini 2.5 Pro for requests to be eligible for caching.

[Official announcement from Google](https://developers.googleblog.com/en/gemini-2-5-models-now-support-implicit-caching)

##### 

To maximize implicit cache hits, keep the initial portion of your message
arrays consistent between requests. Push variations (such as user questions or
dynamic context elements) toward the end of your prompt/requests.

### Pricing Changes for Cached Requests:

- **Cache Writes:** Charged at the input token cost plus 5 minutes of cache storage, calculated as follows:

```
|  |
| --- |
| Cache write cost = Input token price + (Cache storage price × (5 minutes / 60 minutes)) |
```

- **Cache Reads:** Charged at 0.25× the original input token cost.

### Supported Models and Limitations:

Only certain Gemini models support caching. Please consult Google’s [Gemini API Pricing Documentation](https://ai.google.dev/gemini-api/docs/pricing) for the most current details.

Cache Writes have a 5 minute Time-to-Live (TTL) that does not update. After 5 minutes, the cache expires and a new cache must be written.

Gemini models have typically have a 4096 token minimum for cache write to occur. Cached tokens count towards the model’s maximum token usage. Gemini 2.5 Pro has a minimum of 2048 tokens, and Gemini 2.5 Flash has a minimum of 1028 tokens.

### How Gemini Prompt Caching works on OpenRouter:

OpenRouter simplifies Gemini cache management, abstracting away complexities:

- You **do not** need to manually create, update, or delete caches.
- You **do not** need to manage cache names or TTL explicitly.

### How to Enable Gemini Prompt Caching:

Gemini caching in OpenRouter requires you to insert `cache_control` breakpoints explicitly within message content, similar to Anthropic. We recommend using caching primarily for large content pieces (such as CSV files, lengthy character cards, retrieval augmented generation (RAG) data, or extensive textual sources).

##### 

There is not a limit on the number of `cache_control` breakpoints you can
include in your request. OpenRouter will use only the last breakpoint for
Gemini caching. Including multiple breakpoints is safe and can help maintain
compatibility with Anthropic, but only the final one will be used for Gemini.

### Examples:

#### System Message Caching Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "messages": [ |
| 3 | { |
| 4 | "role": "system", |
| 5 | "content": [ |
| 6 | { |
| 7 | "type": "text", |
| 8 | "text": "You are a historian studying the fall of the Roman Empire. Below is an extensive reference book:" |
| 9 | }, |
| 10 | { |
| 11 | "type": "text", |
| 12 | "text": "HUGE TEXT BODY HERE", |
| 13 | "cache_control": { |
| 14 | "type": "ephemeral" |
| 15 | } |
| 16 | } |
| 17 | ] |
| 18 | }, |
| 19 | { |
| 20 | "role": "user", |
| 21 | "content": [ |
| 22 | { |
| 23 | "type": "text", |
| 24 | "text": "What triggered the collapse?" |
| 25 | } |
| 26 | ] |
| 27 | } |
| 28 | ] |
| 29 | } |
```

#### User Message Caching Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "messages": [ |
| 3 | { |
| 4 | "role": "user", |
| 5 | "content": [ |
| 6 | { |
| 7 | "type": "text", |
| 8 | "text": "Based on the book text below:" |
| 9 | }, |
| 10 | { |
| 11 | "type": "text", |
| 12 | "text": "HUGE TEXT BODY HERE", |
| 13 | "cache_control": { |
| 14 | "type": "ephemeral" |
| 15 | } |
| 16 | }, |
| 17 | { |
| 18 | "type": "text", |
| 19 | "text": "List all main characters mentioned in the text above." |
| 20 | } |
| 21 | ] |
| 22 | } |
| 23 | ] |
| 24 | } |
```
