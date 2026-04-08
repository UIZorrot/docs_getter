---
source_url: "https://openrouter.ai/docs/guides/features/structured-outputs"
title: "Structured Outputs | Enforce JSON Schema in OpenRouter API Responses | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:39.177255+00:00"
---
[Features](../presets/index.md)

# Structured Outputs

Return structured data from your models

OpenRouter supports structured outputs for compatible models, ensuring responses follow a specific JSON Schema format. This feature is particularly useful when you need consistent, well-formatted responses that can be reliably parsed by your application.

## Overview

Structured outputs allow you to:

- Enforce specific JSON Schema validation on model responses
- Get consistent, type-safe outputs
- Avoid parsing errors and hallucinated fields
- Simplify response handling in your application

## Using Structured Outputs

To use structured outputs, include a `response_format` parameter in your request, with `type` set to `json_schema` and the `json_schema` object containing your schema:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "messages": [ |
| 3 | { "role": "user", "content": "What's the weather like in London?" } |
| 4 | ], |
| 5 | "response_format": { |
| 6 | "type": "json_schema", |
| 7 | "json_schema": { |
| 8 | "name": "weather", |
| 9 | "strict": true, |
| 10 | "schema": { |
| 11 | "type": "object", |
| 12 | "properties": { |
| 13 | "location": { |
| 14 | "type": "string", |
| 15 | "description": "City or location name" |
| 16 | }, |
| 17 | "temperature": { |
| 18 | "type": "number", |
| 19 | "description": "Temperature in Celsius" |
| 20 | }, |
| 21 | "conditions": { |
| 22 | "type": "string", |
| 23 | "description": "Weather conditions description" |
| 24 | } |
| 25 | }, |
| 26 | "required": ["location", "temperature", "conditions"], |
| 27 | "additionalProperties": false |
| 28 | } |
| 29 | } |
| 30 | } |
| 31 | } |
```

The model will respond with a JSON object that strictly follows your schema:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "location": "London", |
| 3 | "temperature": 18, |
| 4 | "conditions": "Partly cloudy with light drizzle" |
| 5 | } |
```

## Model Support

Structured outputs are supported by select models.

You can find a list of models that support structured outputs on the [models page](https://openrouter.ai/models).

- OpenAI models (GPT-4o and later versions) [Docs](https://platform.openai.com/docs/guides/structured-outputs)
- Google Gemini models [Docs](https://ai.google.dev/gemini-api/docs/structured-output)
- Anthropic models (Sonnet 4.5, Opus 4.1+) [Docs](https://docs.claude.com/en/docs/build-with-claude/structured-outputs)
- Most open-source models
- All Fireworks provided models [Docs](https://docs.fireworks.ai/structured-responses/structured-response-formatting)

To ensure your chosen model supports structured outputs:

1. Check the model’s supported parameters on the [models page](https://openrouter.ai/models)
2. Set `require_parameters: true` in your provider preferences (see [Provider Routing](../../../features/provider-routing/index.md))
3. Include `response_format` and set `type: json_schema` in the required parameters

## Best Practices

1. **Include descriptions**: Add clear descriptions to your schema properties to guide the model
2. **Use strict mode**: Always set `strict: true` to ensure the model follows your schema exactly

## Example Implementation

Here’s a complete example using the Fetch API:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '{{API_KEY_REF}}', |
| 5 | }); |
| 6 |  |
| 7 | const response = await openRouter.chat.send({ |
| 8 | model: '{{MODEL}}', |
| 9 | messages: [ |
| 10 | { role: 'user', content: 'What is the weather like in London?' }, |
| 11 | ], |
| 12 | responseFormat: { |
| 13 | type: 'json_schema', |
| 14 | jsonSchema: { |
| 15 | name: 'weather', |
| 16 | strict: true, |
| 17 | schema: { |
| 18 | type: 'object', |
| 19 | properties: { |
| 20 | location: { |
| 21 | type: 'string', |
| 22 | description: 'City or location name', |
| 23 | }, |
| 24 | temperature: { |
| 25 | type: 'number', |
| 26 | description: 'Temperature in Celsius', |
| 27 | }, |
| 28 | conditions: { |
| 29 | type: 'string', |
| 30 | description: 'Weather conditions description', |
| 31 | }, |
| 32 | }, |
| 33 | required: ['location', 'temperature', 'conditions'], |
| 34 | additionalProperties: false, |
| 35 | }, |
| 36 | }, |
| 37 | }, |
| 38 | stream: false, |
| 39 | }); |
| 40 |  |
| 41 | const weatherInfo = response.choices[0].message.content; |
```

## Streaming with Structured Outputs

Structured outputs are also supported with streaming responses. The model will stream valid partial JSON that, when complete, forms a valid response matching your schema.

To enable streaming with structured outputs, simply add `stream: true` to your request:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "stream": true, |
| 3 | "response_format": { |
| 4 | "type": "json_schema", |
| 5 | // ... rest of your schema |
| 6 | } |
| 7 | } |
```

## Error Handling

When using structured outputs, you may encounter these scenarios:

1. **Model doesn’t support structured outputs**: The request will fail with an error indicating lack of support
2. **Invalid schema**: The model will return an error if your JSON Schema is invalid

## Response Healing

For non-streaming requests using `response_format` with `type: "json_schema"`, you can enable the [Response Healing](../plugins/response-healing/index.md) plugin to reduce the risk of invalid JSON when models return imperfect formatting. Learn more in the [Response Healing documentation](../plugins/response-healing/index.md).
