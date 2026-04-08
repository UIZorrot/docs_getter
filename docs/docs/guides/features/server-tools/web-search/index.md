---
source_url: "https://openrouter.ai/docs/guides/features/server-tools/web-search"
title: "Web Search Server Tool | Real-Time Web Search for Any Model | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:39.040780+00:00"
---
[Features](../../presets/index.md)[Server Tools](../overview/index.md)

# Web Search

Beta

Give any model access to real-time web information

##### Beta

Server tools are currently in beta. The API and behavior may change.

The `openrouter:web_search` server tool gives any model on OpenRouter access to real-time web information. When the model determines it needs current information, it calls the tool with a search query. OpenRouter executes the search and returns results that the model uses to formulate a grounded, cited response.

## How It Works

1. You include `{ "type": "openrouter:web_search" }` in your `tools` array.
2. Based on the user’s prompt, the model decides whether a web search is needed and generates a search query.
3. OpenRouter executes the search using the configured engine (defaults to `auto`, which uses native provider search when available or falls back to [Exa](https://exa.ai/)).
4. The search results (URLs, titles, and content snippets) are returned to the model.
5. The model synthesizes the results into its response. It may search multiple times in a single request if needed.

## Quick Start

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/chat/completions', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | Authorization: 'Bearer {{API_KEY_REF}}', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: '{{MODEL}}', |
| 9 | messages: [ |
| 10 | { |
| 11 | role: 'user', |
| 12 | content: 'What were the major AI announcements this week?' |
| 13 | } |
| 14 | ], |
| 15 | tools: [ |
| 16 | { type: 'openrouter:web_search' } |
| 17 | ] |
| 18 | }), |
| 19 | }); |
| 20 |  |
| 21 | const data = await response.json(); |
| 22 | console.log(data.choices[0].message.content); |
```

## Configuration

The web search tool accepts optional `parameters` to customize search behavior:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "type": "openrouter:web_search", |
| 3 | "parameters": { |
| 4 | "engine": "exa", |
| 5 | "max_results": 5, |
| 6 | "max_total_results": 20, |
| 7 | "search_context_size": "medium", |
| 8 | "allowed_domains": ["example.com"], |
| 9 | "excluded_domains": ["reddit.com"] |
| 10 | } |
| 11 | } |
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `engine` | string | `auto` | Search engine to use: `auto`, `native`, `exa`, `firecrawl`, or `parallel` |
| `max_results` | integer | 5 | Maximum results per search call (1–25). Applies to Exa, Firecrawl, and Parallel engines; ignored with native provider search |
| `max_total_results` | integer | — | Maximum total results across all search calls in a single request. Useful for controlling cost and context size in agentic loops |
| `search_context_size` | string | `medium` | How much context to retrieve per result: `low`, `medium`, or `high`. Only applies to Exa engine |
| `user_location` | object | — | Approximate user location for location-biased results (see below) |
| `allowed_domains` | string[] | — | Limit results to these domains. Supported by Exa, Parallel, and most native providers (see [domain filtering](#domain-filtering)) |
| `excluded_domains` | string[] | — | Exclude results from these domains. Supported by Exa, Parallel, and some native providers (see [domain filtering](#domain-filtering)) |

### User Location

Pass an approximate user location to bias search results geographically:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "type": "openrouter:web_search", |
| 3 | "parameters": { |
| 4 | "user_location": { |
| 5 | "type": "approximate", |
| 6 | "city": "San Francisco", |
| 7 | "region": "California", |
| 8 | "country": "US", |
| 9 | "timezone": "America/Los_Angeles" |
| 10 | } |
| 11 | } |
| 12 | } |
```

All fields within `user_location` are optional.

## Engine Selection

The web search server tool supports multiple search engines:

- **`auto`** (default): Uses native search if the provider supports it, otherwise falls back to Exa
- **`native`**: Forces the provider’s built-in web search (falls back to Exa with a warning if the provider doesn’t support it)
- **`exa`**: Uses [Exa](https://exa.ai/)’s search API, which combines keyword and embeddings-based search
- **`firecrawl`**: Uses [Firecrawl](https://firecrawl.dev/)’s search API (BYOK — bring your own key)
- **`parallel`**: Uses [Parallel](https://parallel.ai/)’s search API

### Engine Capabilities

| Feature | Exa | Firecrawl | Parallel | Native |
| --- | --- | --- | --- | --- |
| **Domain filtering** | Yes | No | Yes | Varies by provider |
| **Context size control** | Yes | No | No | No |
| **API key** | Server-side | BYOK (your key) | Server-side | Provider-handled |

### Firecrawl (BYOK)

Firecrawl uses your own API key. To set it up:

1. Go to your [OpenRouter plugin settings](https://openrouter.ai/settings/plugins) and select Firecrawl as the web search engine
2. Accept the [Firecrawl Terms of Service](https://www.firecrawl.dev/terms-of-service) — this creates a Firecrawl account linked to your email
3. Your account starts with a **free hobby plan and 100,000 credits**

Firecrawl searches use your Firecrawl credits directly — no additional charge from OpenRouter. Domain filtering is not supported with Firecrawl.

### Parallel

[Parallel](https://parallel.ai/) supports domain filtering and uses OpenRouter credits at the same rate as Exa ($4 per 1,000 results).

## Domain Filtering

Restrict which domains appear in search results using `allowed_domains` and `excluded_domains`:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "type": "openrouter:web_search", |
| 3 | "parameters": { |
| 4 | "allowed_domains": ["arxiv.org", "nature.com"], |
| 5 | "excluded_domains": ["reddit.com"] |
| 6 | } |
| 7 | } |
```

| Engine | `allowed_domains` | `excluded_domains` | Notes |
| --- | --- | --- | --- |
| **Exa** | Yes | Yes | Both can be used simultaneously |
| **Parallel** | Yes | Yes | Mutually exclusive |
| **Firecrawl** | No | No | Returns an error if domain filters are set |
| **Native (Anthropic)** | Yes | Yes | Mutually exclusive (`allowed_domains` or `excluded_domains`, not both) |
| **Native (OpenAI)** | Yes | No | `excluded_domains` silently ignored |
| **Native (xAI)** | Yes | Yes | Mutually exclusive |
| **Native (Perplexity)** | No | No | Not supported via server tool path |

## Controlling Total Results

When the model searches multiple times in a single request, use `max_total_results` to cap the cumulative number of results:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "type": "openrouter:web_search", |
| 3 | "parameters": { |
| 4 | "max_results": 5, |
| 5 | "max_total_results": 15 |
| 6 | } |
| 7 | } |
```

Once the limit is reached, subsequent search calls return a message telling the model the limit was hit instead of performing another search. This is useful for controlling cost and context window usage in agentic loops.

## Works with the Responses API

The web search server tool also works with the Responses API:

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | Authorization: 'Bearer {{API_KEY_REF}}', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: '{{MODEL}}', |
| 9 | input: 'What is the current price of Bitcoin?', |
| 10 | tools: [ |
| 11 | { type: 'openrouter:web_search', parameters: { max_results: 3 } } |
| 12 | ] |
| 13 | }), |
| 14 | }); |
| 15 |  |
| 16 | const data = await response.json(); |
| 17 | console.log(data); |
```

## Usage Tracking

Web search usage is reported in the response `usage` object:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "usage": { |
| 3 | "input_tokens": 105, |
| 4 | "output_tokens": 250, |
| 5 | "server_tool_use": { |
| 6 | "web_search_requests": 2 |
| 7 | } |
| 8 | } |
| 9 | } |
```

The `web_search_requests` field counts the total number of search queries the model made during the request.

## Pricing

| Engine | Pricing |
| --- | --- |
| **Exa** | $4 per 1,000 results using OpenRouter credits (default 5 results = max $0.02 per search) |
| **Parallel** | $4 per 1,000 results using OpenRouter credits (same as Exa) |
| **Firecrawl** | Uses your Firecrawl credits directly — no OpenRouter charge |
| **Native** | Passed through from the provider ([OpenAI](https://platform.openai.com/docs/pricing), [Anthropic](https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-search-tool), [Perplexity](https://docs.perplexity.ai/getting-started/pricing), [xAI](https://docs.x.ai/docs/models)) |

All pricing is in addition to standard LLM token costs for processing the search result content.

## Migrating from the Web Search Plugin

##### 

The [web search plugin](../../plugins/web-search/index.md) (`plugins: [{ id: "web" }]`) and the [`:online` variant](../../../routing/model-variants/online/index.md) are deprecated. Use the `openrouter:web_search` server tool instead.

The key differences:

|  | Web Search Plugin (deprecated) | Web Search Server Tool |
| --- | --- | --- |
| **How to enable** | `plugins: [{ id: "web" }]` | `tools: [{ type: "openrouter:web_search" }]` |
| **Who decides to search** | Always searches once | Model decides when/whether to search |
| **Call frequency** | Once per request | 0 to N times per request |
| **Engine options** | Native, Exa, Firecrawl, Parallel | Auto, Native, Exa, Firecrawl, Parallel |
| **Domain filtering** | Yes (Exa, Parallel, some native) | Yes (Exa, Parallel, most native) |
| **Context size control** | Via `web_search_options` | Via `search_context_size` parameter |
| **Total results cap** | No | Yes (`max_total_results`) |
| **Pricing** | Varies by engine | Varies by engine (same rates) |

### Migration example

```
|  |  |
| --- | --- |
| 1 | // Before (deprecated) |
| 2 | { |
| 3 | "model": "openai/gpt-5.2", |
| 4 | "messages": [...], |
| 5 | "plugins": [{ "id": "web", "max_results": 3 }] |
| 6 | } |
| 7 |  |
| 8 | // After |
| 9 | { |
| 10 | "model": "openai/gpt-5.2", |
| 11 | "messages": [...], |
| 12 | "tools": [ |
| 13 | { "type": "openrouter:web_search", "parameters": { "max_results": 3 } } |
| 14 | ] |
| 15 | } |
```

```
|  |  |
| --- | --- |
| 1 | // Before (deprecated) — engine and domain filtering |
| 2 | { |
| 3 | "model": "openai/gpt-5.2", |
| 4 | "messages": [...], |
| 5 | "plugins": [{ |
| 6 | "id": "web", |
| 7 | "engine": "exa", |
| 8 | "max_results": 5, |
| 9 | "include_domains": ["arxiv.org"] |
| 10 | }] |
| 11 | } |
| 12 |  |
| 13 | // After |
| 14 | { |
| 15 | "model": "openai/gpt-5.2", |
| 16 | "messages": [...], |
| 17 | "tools": [{ |
| 18 | "type": "openrouter:web_search", |
| 19 | "parameters": { |
| 20 | "engine": "exa", |
| 21 | "max_results": 5, |
| 22 | "allowed_domains": ["arxiv.org"] |
| 23 | } |
| 24 | }] |
| 25 | } |
```

```
|  |  |
| --- | --- |
| 1 | // Before (deprecated) — :online variant |
| 2 | { |
| 3 | "model": "openai/gpt-5.2:online" |
| 4 | } |
| 5 |  |
| 6 | // After |
| 7 | { |
| 8 | "model": "openai/gpt-5.2", |
| 9 | "tools": [{ "type": "openrouter:web_search" }] |
| 10 | } |
```

## Next Steps

- [Server Tools Overview](../index.md) — Learn about server tools
- [Datetime](../datetime/index.md) — Get the current date and time
- [Tool Calling](../../tool-calling/index.md) — Learn about user-defined tool calling
