---
source_url: "https://openrouter.ai/docs/api/reference/responses/overview"
title: "OpenRouter Responses API Beta | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:30.343110+00:00"
---
[API Guides](../../overview/index.md)[Responses API](index.md)

# Responses API Beta

OpenAI-compatible Responses API (Beta)

##### Beta API

This API is in **beta stage** and may have breaking changes. Use with caution in production environments.

##### Stateless Only

This API is **stateless** - each request is independent and no conversation state is persisted between requests. You must include the full conversation history in each request.

OpenRouter’s Responses API Beta provides OpenAI-compatible access to multiple AI models through a unified interface, designed to be a drop-in replacement for OpenAI’s Responses API. This stateless API offers enhanced capabilities including reasoning, tool calling, and web search integration, with each request being independent and no server-side state persisted.

## Base URL

```
|  |
| --- |
| https://openrouter.ai/api/v1/responses |
```

## Authentication

All requests require authentication using your OpenRouter API key:

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/responses', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | 'Authorization': 'Bearer YOUR_OPENROUTER_API_KEY', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'openai/o4-mini', |
| 9 | input: 'Hello, world!', |
| 10 | }), |
| 11 | }); |
```

## Core Features

### [Basic Usage](../basic-usage/index.md)

Learn the fundamentals of making requests with simple text input and handling responses.

### [Reasoning](../reasoning/index.md)

Access advanced reasoning capabilities with configurable effort levels and encrypted reasoning chains.

### [Tool Calling](../tool-calling/index.md)

Integrate function calling with support for parallel execution and complex tool interactions.

### [Web Search](../web-search/index.md)

Enable web search capabilities with real-time information retrieval and citation annotations.

## Error Handling

The API returns structured error responses:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "error": { |
| 3 | "code": "invalid_prompt", |
| 4 | "message": "Missing required parameter: 'model'." |
| 5 | }, |
| 6 | "metadata": null |
| 7 | } |
```

For comprehensive error handling guidance, see [Error Handling](../error-handling/index.md).

## Rate Limits

Standard OpenRouter rate limits apply. See [API Limits](../../../../api-reference/limits/index.md) for details.
