---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/chatrequest"
title: "ChatRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:14.746712+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ChatRequest - TypeScript SDK

ChatRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Chat completion request parameters

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ChatRequest } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ChatRequest = { |
| 4 | messages: [ |
| 5 | { |
| 6 | role: "system", |
| 7 | content: "You are a helpful assistant.", |
| 8 | }, |
| 9 | { |
| 10 | role: "user", |
| 11 | content: "What is the capital of France?", |
| 12 | }, |
| 13 | ], |
| 14 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `provider` | [models.ProviderPreferences](../providerpreferences/index.md) | ➖ | When multiple model providers are available, optionally indicate your routing preference. | `{"allow_fallbacks": true}` |
| `plugins` | *models.ChatRequestPlugin*[] | ➖ | Plugins you want to enable for this request, including their settings. |  |
| `user` | *string* | ➖ | Unique user identifier | user-123 |
| `sessionId` | *string* | ➖ | A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 256 characters. |  |
| `trace` | [models.TraceConfig](../traceconfig/index.md) | ➖ | Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations. | `{"trace_id": "trace-abc123","trace_name": "my-app-trace"}` |
| `messages` | *models.ChatMessages*[] | ✔️ | List of messages for the conversation | [ `{"role": "user","content": "Hello!"}` ] |
| `model` | *string* | ➖ | Model to use for completion | openai/gpt-4 |
| `models` | *string*[] | ➖ | Models to use for completion | [ “openai/gpt-4”, “openai/gpt-4o” ] |
| `frequencyPenalty` | *number* | ➖ | Frequency penalty (-2.0 to 2.0) | 0 |
| `logitBias` | `Record<string, *number*>` | ➖ | Token logit bias adjustments | `{"50256": -100}` |
| `logprobs` | *boolean* | ➖ | Return log probabilities | false |
| `topLogprobs` | *number* | ➖ | Number of top log probabilities to return (0-20) | 5 |
| `maxCompletionTokens` | *number* | ➖ | Maximum tokens in completion | 100 |
| `maxTokens` | *number* | ➖ | Maximum tokens (deprecated, use max\_completion\_tokens). Note: some providers enforce a minimum of 16. | 100 |
| `metadata` | `Record<string, *string*>` | ➖ | Key-value pairs for additional object information (max 16 pairs, 64 char keys, 512 char values) | `{"user_id": "user-123","session_id": "session-456"}` |
| `presencePenalty` | *number* | ➖ | Presence penalty (-2.0 to 2.0) | 0 |
| `reasoning` | [models.Reasoning](../reasoning/index.md) | ➖ | Configuration options for reasoning models | `{"effort": "medium","summary": "concise"}` |
| `responseFormat` | *models.ResponseFormat* | ➖ | Response format configuration | `{"type": "json_object"}` |
| `seed` | *number* | ➖ | Random seed for deterministic outputs | 42 |
| `stop` | *models.Stop* | ➖ | Stop sequences (up to 4) | [ "" ] |
| `stream` | *boolean* | ➖ | Enable streaming response | false |
| `streamOptions` | [models.ChatStreamOptions](../chatstreamoptions/index.md) | ➖ | Streaming configuration options | `{"include_usage": true}` |
| `temperature` | *number* | ➖ | Sampling temperature (0-2) | 0.7 |
| `parallelToolCalls` | *boolean* | ➖ | Whether to enable parallel function calling during tool use. When true, the model may generate multiple tool calls in a single response. | true |
| `toolChoice` | *models.ChatToolChoice* | ➖ | Tool choice configuration | auto |
| `tools` | *models.ChatFunctionTool*[] | ➖ | Available tools for function calling | [ `{"type": "function","function": {"name": "get_weather","description": "Get weather"}` } ] |
| `topP` | *number* | ➖ | Nucleus sampling parameter (0-1) | 1 |
| `debug` | [models.ChatDebugOptions](../chatdebugoptions/index.md) | ➖ | Debug options for inspecting request transformations (streaming only) | `{"echo_upstream_body": true}` |
| `imageConfig` | `Record<string, *models.ChatRequestImageConfig*>` | ➖ | Provider-specific image configuration options. Keys and values vary by model/provider. See [https://openrouter.ai/docs/guides/overview/multimodal/image-generation](../../../../../guides/overview/multimodal/image-generation/index.md) for more details. | `{"aspect_ratio": "16:9"}` |
| `modalities` | [models.Modality](../modality/index.md)[] | ➖ | Output modalities for the response. Supported values are “text”, “image”, and “audio”. | [ “text”, “image” ] |
| `cacheControl` | [models.AnthropicCacheControlDirective](../anthropiccachecontroldirective/index.md) | ➖ | N/A | `{"type": "ephemeral"}` |
| `serviceTier` | [models.ChatRequestServiceTier](../chatrequestservicetier/index.md) | ➖ | The service tier to use for processing this request. | auto |
