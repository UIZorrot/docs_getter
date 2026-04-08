---
source_url: "https://openrouter.ai/docs/guides/administration/usage-accounting"
title: "Usage Accounting | Track AI Model Usage with OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:54.340476+00:00"
---
[Guides](../activity-export/index.md)[Administration](../activity-export/index.md)

# Usage Accounting

The OpenRouter API provides built-in **Usage Accounting** that allows you to track AI model usage without making additional API calls. This feature provides detailed information about token counts, costs, and caching status directly in your API responses.

## Usage Information

OpenRouter automatically returns detailed usage information with every response, including:

1. Prompt and completion token counts using the model’s native tokenizer
2. Cost in credits
3. Reasoning token counts (if applicable)
4. Cached token counts (if available)

This information is included in the last SSE message for streaming responses, or in the complete response for non-streaming requests. No additional parameters are required.

##### Deprecated Parameters

The `usage: { include: true }` and `stream_options: { include_usage: true }` parameters are deprecated and have no effect. Full usage details are now always included automatically in every response.

## Response Format

Every response includes a `usage` object with detailed token information:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "object": "chat.completion.chunk", |
| 3 | "usage": { |
| 4 | "completion_tokens": 2, |
| 5 | "completion_tokens_details": { |
| 6 | "reasoning_tokens": 0 |
| 7 | }, |
| 8 | "cost": 0.95, |
| 9 | "cost_details": { |
| 10 | "upstream_inference_cost": 19 |
| 11 | }, |
| 12 | "prompt_tokens": 194, |
| 13 | "prompt_tokens_details": { |
| 14 | "cached_tokens": 0, |
| 15 | "cache_write_tokens": 100, |
| 16 | "audio_tokens": 0 |
| 17 | }, |
| 18 | "total_tokens": 196 |
| 19 | } |
| 20 | } |
```

`cached_tokens` is the number of tokens that were *read* from the cache. `cache_write_tokens` is the number of tokens that were *written* to the cache (only returned for models with explicit caching and cache write pricing).

## Cost Breakdown

The usage response includes detailed cost information:

- `cost`: The total amount charged to your account
- `cost_details.upstream_inference_cost`: The actual cost charged by the upstream AI provider

**Note:** The `upstream_inference_cost` field only applies to BYOK (Bring Your Own Key) requests.

## Benefits

1. **Efficiency**: Get usage information without making separate API calls
2. **Accuracy**: Token counts are calculated using the model’s native tokenizer
3. **Transparency**: Track costs and cached token usage in real-time
4. **Detailed Breakdown**: Separate counts for prompt, completion, reasoning, and cached tokens

## Best Practices

1. Use the usage data to monitor token consumption and costs
2. Consider tracking usage in development to optimize token usage before production
3. Use the cached token information to optimize your application’s performance

## Alternative: Getting Usage via Generation ID

You can also retrieve usage information asynchronously by using the generation ID returned from your API calls. This is particularly useful when you want to fetch usage statistics after the completion has finished or when you need to audit historical usage.

To use this method:

1. Make your chat completion request as normal
2. Note the `id` field in the response
3. Use that ID to fetch usage information via the `/generation` endpoint

For more details on this approach, see the [Get a Generation](../../../api-reference/get-a-generation/index.md) documentation.

## Examples

### Basic Usage with Token Tracking

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
| 10 | { |
| 11 | role: 'user', |
| 12 | content: 'What is the capital of France?', |
| 13 | }, |
| 14 | ], |
| 15 | }); |
| 16 |  |
| 17 | console.log('Response:', response.choices[0].message.content); |
| 18 | // Usage is always included automatically |
| 19 | console.log('Usage Stats:', response.usage); |
```

### Streaming with Usage Information

This example shows how to handle usage information in streaming mode:

```
|  |  |
| --- | --- |
| 1 | from openai import OpenAI |
| 2 |  |
| 3 | client = OpenAI( |
| 4 | base_url="https://openrouter.ai/api/v1", |
| 5 | api_key="{{API_KEY_REF}}", |
| 6 | ) |
| 7 |  |
| 8 | def chat_completion_streaming(messages): |
| 9 | response = client.chat.completions.create( |
| 10 | model="{{MODEL}}", |
| 11 | messages=messages, |
| 12 | stream=True |
| 13 | ) |
| 14 | return response |
| 15 |  |
| 16 | # Usage is always included in the final chunk when streaming |
| 17 | for chunk in chat_completion_streaming([ |
| 18 | {"role": "user", "content": "Write a haiku about Paris."} |
| 19 | ]): |
| 20 | if hasattr(chunk, 'usage') and chunk.usage: |
| 21 | if hasattr(chunk.usage, 'total_tokens'): |
| 22 | print(f"\nUsage Statistics:") |
| 23 | print(f"Total Tokens: {chunk.usage.total_tokens}") |
| 24 | print(f"Prompt Tokens: {chunk.usage.prompt_tokens}") |
| 25 | print(f"Completion Tokens: {chunk.usage.completion_tokens}") |
| 26 | print(f"Cost: {chunk.usage.cost} credits") |
| 27 | elif chunk.choices and chunk.choices[0].delta.content: |
| 28 | print(chunk.choices[0].delta.content, end="") |
```
