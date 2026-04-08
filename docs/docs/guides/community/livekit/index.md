---
source_url: "https://openrouter.ai/docs/guides/community/livekit"
title: "LiveKit Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:34.822667+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# LiveKit

Using OpenRouter with LiveKit Agents

## Using LiveKit Agents

[LiveKit Agents](https://docs.livekit.io/agents) is an open-source framework for building voice AI agents. The OpenRouter plugin allows you to access 300+ AI models from multiple providers through a unified API, with automatic fallback support and intelligent routing.

### Installation

Install the OpenAI plugin to add OpenRouter support:

```
|  |  |
| --- | --- |
| $ | uv add "livekit-agents[openai]~=1.2" |
```

### Authentication

The OpenRouter plugin requires an [OpenRouter API key](https://openrouter.ai/settings/keys). Set `OPENROUTER_API_KEY` in your `.env` file.

### Basic Usage

Create an OpenRouter LLM using the `with_openrouter` method:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | session = AgentSession( |
| 4 | llm=openai.LLM.with_openrouter(model="anthropic/claude-sonnet-4.5"), |
| 5 | # ... tts, stt, vad, turn_detection, etc. |
| 6 | ) |
```

### Advanced Features

#### Fallback Models

Configure multiple fallback models to use if the primary model is unavailable:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | llm = openai.LLM.with_openrouter( |
| 4 | model="openai/gpt-4o", |
| 5 | fallback_models=[ |
| 6 | "anthropic/claude-sonnet-4", |
| 7 | "openai/gpt-5-mini", |
| 8 | ], |
| 9 | ) |
```

#### Provider Routing

Control which providers are used for model inference:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | llm = openai.LLM.with_openrouter( |
| 4 | model="deepseek/deepseek-chat-v3.1", |
| 5 | provider={ |
| 6 | "order": ["novita/fp8", "gmicloud/fp8", "google-vertex"], |
| 7 | "allow_fallbacks": True, |
| 8 | "sort": "latency", |
| 9 | }, |
| 10 | ) |
```

#### Web Search Plugin

Enable OpenRouter’s web search capabilities:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | llm = openai.LLM.with_openrouter( |
| 4 | model="google/gemini-3-flash-preview", |
| 5 | plugins=[ |
| 6 | openai.OpenRouterWebPlugin( |
| 7 | max_results=5, |
| 8 | search_prompt="Search for relevant information", |
| 9 | ) |
| 10 | ], |
| 11 | ) |
```

#### Analytics Integration

Include site and app information for OpenRouter analytics:

Python

```
|  |  |
| --- | --- |
| 1 | from livekit.plugins import openai |
| 2 |  |
| 3 | llm = openai.LLM.with_openrouter( |
| 4 | model="openrouter/auto", |
| 5 | site_url="https://myapp.com", |
| 6 | app_name="My Voice Agent", |
| 7 | ) |
```

### Resources

- [LiveKit OpenRouter Plugin Documentation](https://docs.livekit.io/agents/models/llm/plugins/openrouter)
- [LiveKit Agents GitHub](https://github.com/livekit/agents)
- [OpenRouter Models](https://openrouter.ai/models)
