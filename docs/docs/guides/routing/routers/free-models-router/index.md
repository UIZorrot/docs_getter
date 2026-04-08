---
source_url: "https://openrouter.ai/docs/guides/routing/routers/free-models-router"
title: "Free Models Router | Zero-Cost AI Inference | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:42.104807+00:00"
---
[Models & Routing](../../model-fallbacks/index.md)[Routers](../auto-router/index.md)

# Free Models Router

Get free AI inference by routing to available free models

The [Free Models Router](https://openrouter.ai/openrouter/free) (`openrouter/free`) automatically selects a free model at random from the available free models on OpenRouter. The router intelligently filters for models that support the features your request needs, such as image understanding, tool calling, and structured outputs.

## Overview

Instead of manually choosing a specific free model, let the Free Models Router handle model selection for you. This is ideal for experimentation, learning, and low-volume use cases where you want zero-cost inference without worrying about which specific model to use.

To try the Free Models Router without writing any code, see the [Chat Playground guide](../../../get-started/free-models-router-playground/index.md).

## Usage

Set your model to `openrouter/free`:

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
| 8 | model: 'openrouter/free', |
| 9 | messages: [ |
| 10 | { |
| 11 | role: 'user', |
| 12 | content: 'Hello! What can you help me with today?', |
| 13 | }, |
| 14 | ], |
| 15 | }); |
| 16 |  |
| 17 | console.log(completion.choices[0].message.content); |
| 18 | // Check which model was selected |
| 19 | console.log('Model used:', completion.model); |
```

## Response

The response includes the `model` field showing which free model was actually used:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "id": "gen-...", |
| 3 | "model": "upstage/solar-pro-3:free", |
| 4 | "choices": [ |
| 5 | { |
| 6 | "message": { |
| 7 | "role": "assistant", |
| 8 | "content": "..." |
| 9 | } |
| 10 | } |
| 11 | ], |
| 12 | "usage": { |
| 13 | "prompt_tokens": 12, |
| 14 | "completion_tokens": 85, |
| 15 | "total_tokens": 97 |
| 16 | } |
| 17 | } |
```

## How It Works

1. **Request Analysis**: Your request is analyzed to determine required capabilities (e.g., vision, tool calling, structured outputs)
2. **Model Filtering**: The router filters available free models to those supporting your request’s requirements
3. **Random Selection**: A model is randomly selected from the filtered pool
4. **Request Forwarding**: Your request is forwarded to the selected free model
5. **Response Tracking**: The response includes metadata showing which model was used

## Available Free Models

The Free Models Router selects from all currently available free models on OpenRouter. Some popular options include:

##### 

Free model availability changes frequently. Check the [models page](https://openrouter.ai/models) for the current list of free models.

- **DeepSeek R1 (free)** - DeepSeek’s reasoning model
- **Llama models (free)** - Various Meta Llama models
- **Qwen models (free)** - Alibaba’s Qwen family
- And other community-contributed free models

## Pricing

The Free Models Router is completely free. There is no charge for:

- Using the router itself
- Requests routed to free models

## Use Cases

- **Learning and experimentation**: Try AI capabilities without any cost
- **Prototyping**: Build and test applications before committing to paid models
- **Low-volume applications**: Suitable for personal projects or demos
- **Education**: Perfect for students and educators exploring AI

## Limitations

- **Rate limits**: Free models may have lower rate limits than paid models
- **Availability**: Free model availability can vary; some may be temporarily unavailable
- **Performance**: Free models may have higher latency during peak usage
- **Model selection**: You cannot control which specific model is selected (use the `:free` variant suffix on a specific model if you need a particular free model)

## Selecting Specific Free Models

If you prefer to use a specific free model rather than random selection, you can:

1. **Use the `:free` variant**: Append `:free` to any model that has a free variant:

   ```
   |  |  |
   | --- | --- |
   | 1 | { |
   | 2 | "model": "meta-llama/llama-3.2-3b-instruct:free" |
   | 3 | } |
   ```
2. **Browse free models**: Visit the [models page](https://openrouter.ai/models) to see all available free models and select one directly.

## Related

- [Free Models Router in Chat Playground](../../../get-started/free-models-router-playground/index.md) - Try the router without writing code
- [Free Variant](../../model-variants/free/index.md) - Use the `:free` suffix for specific models
- [Auto Router](../auto-router/index.md) - Intelligent model selection (paid models)
- [Body Builder](../body-builder/index.md) - Generate multiple parallel API requests
- [Model Fallbacks](../../model-fallbacks/index.md) - Configure fallback models
