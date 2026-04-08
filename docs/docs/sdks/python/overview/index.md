---
source_url: "https://openrouter.ai/docs/sdks/python/overview"
title: "OpenRouter Python SDK | Complete Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:45.946572+00:00"
---
[Python SDK](index.md)

# Python SDK

Official OpenRouter Python SDK documentation

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

The OpenRouter Python SDK is a type-safe toolkit for building AI applications with access to 300+ language models through a unified API.

## Why use the OpenRouter SDK?

Integrating AI models into applications involves handling different provider APIs, managing model-specific requirements, and avoiding common implementation mistakes. The OpenRouter SDK standardizes these integrations and protects you from footguns.

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | api_key=os.getenv("OPENROUTER_API_KEY") |
| 6 | ) as client: |
| 7 | response = client.chat.send( |
| 8 | model="minimax/minimax-m2", |
| 9 | messages=[ |
| 10 | {"role": "user", "content": "Explain quantum computing"} |
| 11 | ] |
| 12 | ) |
```

The SDK provides three core benefits:

### Auto-generated from API specifications

The SDK is automatically generated from OpenRouter’s OpenAPI specs and updated with every API change. New models, parameters, and features appear in your IDE autocomplete immediately. No manual updates. No version drift.

```
|  |  |
| --- | --- |
| 1 | # When new models launch, they're available instantly |
| 2 | response = client.chat.send( |
| 3 | model="minimax/minimax-m2" |
| 4 | ) |
```

### Type-safe by default

Every parameter, response field, and configuration option is fully typed with Python type hints and validated with Pydantic. Invalid configurations are caught at runtime with clear error messages.

```
|  |  |
| --- | --- |
| 1 | response = client.chat.send( |
| 2 | model="minimax/minimax-m2", |
| 3 | messages=[ |
| 4 | {"role": "user", "content": "Hello"} |
| 5 | # ← Pydantic validates message structure |
| 6 | ], |
| 7 | temperature=0.7,  # ← Type-checked and validated |
| 8 | stream=True       # ← Response type changes based on this |
| 9 | ) |
```

**Actionable error messages:**

```
|  |  |
| --- | --- |
| 1 | # Instead of generic errors, get specific guidance: |
| 2 | # "Model 'openai/o1-preview' requires at least 2 messages. |
| 3 | #  You provided 1 message. Add a system or user message." |
```

**Type-safe streaming:**

```
|  |  |
| --- | --- |
| 1 | stream = client.chat.send( |
| 2 | model="minimax/minimax-m2", |
| 3 | messages=[{"role": "user", "content": "Write a story"}], |
| 4 | stream=True |
| 5 | ) |
| 6 |  |
| 7 | for event in stream: |
| 8 | # Full type information for streaming responses |
| 9 | content = event.choices[0].delta.content if event.choices else None |
```

**Async support:**

```
|  |  |
| --- | --- |
| 1 | import asyncio |
| 2 |  |
| 3 | async def main(): |
| 4 | async with OpenRouter( |
| 5 | api_key=os.getenv("OPENROUTER_API_KEY") |
| 6 | ) as client: |
| 7 | response = await client.chat.send_async( |
| 8 | model="minimax/minimax-m2", |
| 9 | messages=[{"role": "user", "content": "Hello"}] |
| 10 | ) |
| 11 | print(response.choices[0].message.content) |
| 12 |  |
| 13 | asyncio.run(main()) |
```

## Installation

```
|  |  |
| --- | --- |
| $ | # Using uv (recommended) |
| $ | uv add openrouter |
| $ |  |
| $ | # Using pip |
| $ | pip install openrouter |
| $ |  |
| $ | # Using poetry |
| $ | poetry add openrouter |
```

**Requirements:** Python 3.9 or higher

Get your API key from [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys).

## Quick start

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | api_key=os.getenv("OPENROUTER_API_KEY") |
| 6 | ) as client: |
| 7 | response = client.chat.send( |
| 8 | model="minimax/minimax-m2", |
| 9 | messages=[ |
| 10 | {"role": "user", "content": "Hello!"} |
| 11 | ] |
| 12 | ) |
| 13 |  |
| 14 | print(response.choices[0].message.content) |
```
