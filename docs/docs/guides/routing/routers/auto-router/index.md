---
source_url: "https://openrouter.ai/docs/guides/routing/routers/auto-router"
title: "Auto Router | Smart AI Model Selection | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:57.783959+00:00"
---
[Models & Routing](../../model-fallbacks/index.md)[Routers](index.md)

# Auto Router

Automatically select the best model for your prompt

The [Auto Router](https://openrouter.ai/openrouter/auto) (`openrouter/auto`) automatically selects the best model for your prompt, powered by [NotDiamond](https://www.notdiamond.ai/).

## Overview

Instead of manually choosing a model, let the Auto Router analyze your prompt and select the optimal model from a curated set of high-quality options. The router considers factors like prompt complexity, task type, and model capabilities.

## Usage

Set your model to `openrouter/auto`:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'openrouter/auto', |
| 9 | messages: [ |
| 10 | { |
| 11 | role: 'user', |
| 12 | content: 'Explain quantum entanglement in simple terms', |
| 13 | }, |
| 14 | ], |
| 15 | }); |
| 16 |  |
| 17 | console.log(completion.choices[0].message.content); |
| 18 | // Check which model was selected |
| 19 | console.log('Model used:', completion.model); |
```

## Response

The response includes the `model` field showing which model was actually used:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "id": "gen-...", |
| 3 | "model": "anthropic/claude-sonnet-4.5",  // The model that was selected |
| 4 | "choices": [ |
| 5 | { |
| 6 | "message": { |
| 7 | "role": "assistant", |
| 8 | "content": "..." |
| 9 | } |
| 10 | } |
| 11 | ], |
| 12 | "usage": { |
| 13 | "prompt_tokens": 15, |
| 14 | "completion_tokens": 150, |
| 15 | "total_tokens": 165 |
| 16 | } |
| 17 | } |
```

## How It Works

1. **Prompt Analysis**: Your prompt is analyzed by NotDiamond’s routing system
2. **Model Selection**: The optimal model is selected based on the task requirements
3. **Request Forwarding**: Your request is forwarded to the selected model
4. **Response Tracking**: The response includes metadata showing which model was used

## Supported Models

The Auto Router selects from a curated set of high-quality models including:

##### 

Model slugs change as new versions are released. The examples below are current as of December 4, 2025. Check the [models page](https://openrouter.ai/models) for the latest available models.

- Claude Sonnet 4.5 (`anthropic/claude-sonnet-4.5`)
- Claude Opus 4.5 (`anthropic/claude-opus-4.5`)
- GPT-5.1 (`openai/gpt-5.1`)
- Gemini 3.1 Pro (`google/gemini-3.1-pro-preview`)
- DeepSeek 3.2 (`deepseek/deepseek-v3.2`)
- And other top-performing models

The exact model pool may be updated as new models become available.

## Configuring Allowed Models

You can restrict which models the Auto Router can select from using the `plugins` parameter. This is useful when you want to limit routing to specific providers or model families.

### Via API Request

Use wildcard patterns to filter models. For example, `anthropic/*` matches all Anthropic models:

```
|  |  |
| --- | --- |
| 1 | const completion = await openRouter.chat.send({ |
| 2 | model: 'openrouter/auto', |
| 3 | messages: [ |
| 4 | { |
| 5 | role: 'user', |
| 6 | content: 'Explain quantum entanglement', |
| 7 | }, |
| 8 | ], |
| 9 | plugins: [ |
| 10 | { |
| 11 | id: 'auto-router', |
| 12 | allowed_models: ['anthropic/*', 'openai/gpt-5.1'], |
| 13 | }, |
| 14 | ], |
| 15 | }); |
```

### Via Settings UI

You can also configure default allowed models in your [Plugin Settings](https://openrouter.ai/settings/plugins):

1. Navigate to **Settings > Plugins**
2. Find **Auto Router** and click the configure button
3. Enter model patterns (one per line)
4. Save your settings

These defaults apply to all your API requests unless overridden per-request.

### Pattern Syntax

| Pattern | Matches |
| --- | --- |
| `anthropic/*` | All Anthropic models |
| `openai/gpt-5*` | All GPT-5 variants |
| `google/*` | All Google models |
| `openai/gpt-5.1` | Exact match only |
| `*/claude-*` | Any provider with claude in model name |

When no patterns are configured, the Auto Router uses all supported models.

## Pricing

You pay the standard rate for whichever model is selected. There is no additional fee for using the Auto Router.

## Use Cases

- **General-purpose applications**: When you don’t know what types of prompts users will send
- **Cost optimization**: Let the router choose efficient models for simpler tasks
- **Quality optimization**: Ensure complex prompts get routed to capable models
- **Experimentation**: Discover which models work best for your use case

## Limitations

- The router requires `messages` format (not `prompt`)
- Streaming is supported
- All standard OpenRouter features (tool calling, etc.) work with the selected model

## Related

- [Body Builder](../body-builder/index.md) - Generate multiple parallel API requests
- [Model Fallbacks](../../model-fallbacks/index.md) - Configure fallback models
- [Provider Selection](../../provider-selection/index.md) - Control which providers are used
