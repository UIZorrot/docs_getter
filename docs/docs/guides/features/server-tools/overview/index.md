---
source_url: "https://openrouter.ai/docs/guides/features/server-tools/overview"
title: "Server Tools | Model-Callable Tools Operated by OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:56.729939+00:00"
---
[Features](../../presets/index.md)[Server Tools](index.md)

# Server Tools

Beta

Tools operated by OpenRouter that models can call during request

##### Beta

Server tools are currently in beta. The API and behavior may change.

Server tools are specialized tools operated by OpenRouter that any model can call during a request. When a model decides to use a server tool, OpenRouter executes it server-side and returns the result to the model — no client-side implementation needed.

## Server Tools vs Plugins vs User-Defined Tools

|  | Server Tools | Plugins | User-Defined Tools |
| --- | --- | --- | --- |
| **Who decides to use it** | The model | Always runs | The model |
| **Who executes it** | OpenRouter | OpenRouter | Your application |
| **Call frequency** | 0 to N times per request | Once per request | 0 to N times per request |
| **Specified via** | `tools` array | `plugins` array | `tools` array |
| **Type prefix** | `openrouter:*` | N/A | `function` |

**Server tools** are tools the model can invoke zero or more times during a request. OpenRouter handles execution transparently.

**Plugins** inject or mutate a request or response to add functionality (e.g. response healing, PDF parsing). They always run once when enabled.

**User-defined tools** are standard function-calling tools where the model suggests a call and *your* application executes it.

## Available Server Tools

| Tool | Type | Description |
| --- | --- | --- |
| [**Web Search**](../web-search/index.md) | `openrouter:web_search` | Search the web for current information |
| [**Datetime**](../datetime/index.md) | `openrouter:datetime` | Get the current date and time |

## How Server Tools Work

1. You include one or more server tools in the `tools` array of your API request.
2. The model decides whether and when to call each server tool based on the user’s prompt.
3. OpenRouter intercepts the tool call, executes it server-side, and returns the result to the model.
4. The model uses the result to formulate its response. It may call the tool again if needed.

Server tools work alongside your own user-defined tools — you can include both in the same request.

## Quick Start

Add server tools to the `tools` array using the `openrouter:` type prefix:

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
| 12 | content: 'What are the latest developments in AI?' |
| 13 | } |
| 14 | ], |
| 15 | tools: [ |
| 16 | { type: 'openrouter:web_search' }, |
| 17 | { type: 'openrouter:datetime' } |
| 18 | ] |
| 19 | }), |
| 20 | }); |
| 21 |  |
| 22 | const data = await response.json(); |
| 23 | console.log(data.choices[0].message.content); |
```

## Combining with User-Defined Tools

Server tools and user-defined tools can be used in the same request:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2", |
| 3 | "messages": [...], |
| 4 | "tools": [ |
| 5 | { "type": "openrouter:web_search", "parameters": { "max_results": 3 } }, |
| 6 | { "type": "openrouter:datetime" }, |
| 7 | { |
| 8 | "type": "function", |
| 9 | "function": { |
| 10 | "name": "get_stock_price", |
| 11 | "description": "Get the current stock price for a ticker symbol", |
| 12 | "parameters": { |
| 13 | "type": "object", |
| 14 | "properties": { |
| 15 | "ticker": { "type": "string" } |
| 16 | }, |
| 17 | "required": ["ticker"] |
| 18 | } |
| 19 | } |
| 20 | } |
| 21 | ] |
| 22 | } |
```

The model can call any combination of server tools and user-defined tools. OpenRouter executes the server tools automatically, while your application handles the user-defined tool calls as usual.

## Usage Tracking

Server tool usage is tracked in the response `usage` object:

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

## Next Steps

- [Web Search](../web-search/index.md) — Search the web for real-time information
- [Datetime](../datetime/index.md) — Get the current date and time
- [Tool Calling](../../tool-calling/index.md) — Learn about user-defined tool calling
