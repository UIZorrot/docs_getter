---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/chat"
title: "Chat | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:43.358661+00:00"
---
[Python SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Chat - Python SDK

Chat method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

### Available Operations

- [send](#send) - Create a chat completion

## send

Sends a request for a model response for the given chat conversation. Supports both streaming and non-streaming modes.

### Example Usage

```
|  |  |
| --- | --- |
| 1 | from openrouter import OpenRouter |
| 2 | import os |
| 3 |  |
| 4 | with OpenRouter( |
| 5 | http_referer="<value>", |
| 6 | x_open_router_title="<value>", |
| 7 | x_open_router_categories="<value>", |
| 8 | api_key=os.getenv("OPENROUTER_API_KEY", ""), |
| 9 | ) as open_router: |
| 10 |  |
| 11 | res = open_router.chat.send(messages=[ |
| 12 | { |
| 13 | "role": "system", |
| 14 | "content": "You are a helpful assistant.", |
| 15 | }, |
| 16 | { |
| 17 | "role": "user", |
| 18 | "content": "What is the capital of France?", |
| 19 | }, |
| 20 | ], model="openai/gpt-4", max_tokens=150, stream=False, temperature=0.7) |
| 21 |  |
| 22 | with res as event_stream: |
| 23 | for event in event_stream: |
| 24 | # handle event |
| 25 | print(event, flush=True) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `messages` | List[[components.ChatMessages](../components/chatmessages/index.md)] | ✔️ | List of messages for the conversation | [ `{"role": "user","content": "Hello!"}` ] |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `provider` | [OptionalNullable[components.ProviderPreferences]](../../../components/providerpreferences.md/index.md) | ➖ | When multiple model providers are available, optionally indicate your routing preference. | `{"allow_fallbacks": true}` |
| `plugins` | List[[components.ChatRequestPlugin](../components/chatrequestplugin/index.md)] | ➖ | Plugins you want to enable for this request, including their settings. |  |
| `user` | *Optional[str]* | ➖ | Unique user identifier | user-123 |
| `session_id` | *Optional[str]* | ➖ | A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 256 characters. |  |
| `trace` | [Optional[components.TraceConfig]](../../../components/traceconfig.md/index.md) | ➖ | Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations. | `{"trace_id": "trace-abc123","trace_name": "my-app-trace"}` |
| `model` | *Optional[str]* | ➖ | Model to use for completion | openai/gpt-4 |
| `models` | List[*str*] | ➖ | Models to use for completion | [ “openai/gpt-4”, “openai/gpt-4o” ] |
| `frequency_penalty` | *Optional[float]* | ➖ | Frequency penalty (-2.0 to 2.0) | 0 |
| `logit_bias` | Dict[str, *float*] | ➖ | Token logit bias adjustments | `{"50256": -100}` |
| `logprobs` | *OptionalNullable[bool]* | ➖ | Return log probabilities | false |
| `top_logprobs` | *Optional[int]* | ➖ | Number of top log probabilities to return (0-20) | 5 |
| `max_completion_tokens` | *Optional[int]* | ➖ | Maximum tokens in completion | 100 |
| `max_tokens` | *Optional[int]* | ➖ | Maximum tokens (deprecated, use max\_completion\_tokens). Note: some providers enforce a minimum of 16. | 100 |
| `metadata` | Dict[str, *str*] | ➖ | Key-value pairs for additional object information (max 16 pairs, 64 char keys, 512 char values) | `{"user_id": "user-123","session_id": "session-456"}` |
| `presence_penalty` | *Optional[float]* | ➖ | Presence penalty (-2.0 to 2.0) | 0 |
| `reasoning` | [Optional[components.Reasoning]](../../../components/reasoning.md/index.md) | ➖ | Configuration options for reasoning models | `{"effort": "medium","summary": "concise"}` |
| `response_format` | [Optional[components.ResponseFormat]](../../../components/responseformat.md/index.md) | ➖ | Response format configuration | `{"type": "json_object"}` |
| `seed` | *Optional[int]* | ➖ | Random seed for deterministic outputs | 42 |
| `stop` | [OptionalNullable[components.Stop]](../../../components/stop.md/index.md) | ➖ | Stop sequences (up to 4) | [ "" ] |
| `stream` | *Optional[bool]* | ➖ | Enable streaming response | false |
| `stream_options` | [OptionalNullable[components.ChatStreamOptions]](../../../components/chatstreamoptions.md/index.md) | ➖ | Streaming configuration options | `{"include_usage": true}` |
| `temperature` | *Optional[float]* | ➖ | Sampling temperature (0-2) | 0.7 |
| `parallel_tool_calls` | *OptionalNullable[bool]* | ➖ | Whether to enable parallel function calling during tool use. When true, the model may generate multiple tool calls in a single response. | true |
| `tool_choice` | [Optional[components.ChatToolChoice]](../../../components/chattoolchoice.md/index.md) | ➖ | Tool choice configuration | auto |
| `tools` | List[[components.ChatFunctionTool](../components/chatfunctiontool/index.md)] | ➖ | Available tools for function calling | [ `{"type": "function","function": {"name": "get_weather","description": "Get weather"}` } ] |
| `top_p` | *Optional[float]* | ➖ | Nucleus sampling parameter (0-1) | 1 |
| `debug` | [Optional[components.ChatDebugOptions]](../../../components/chatdebugoptions.md/index.md) | ➖ | Debug options for inspecting request transformations (streaming only) | `{"echo_upstream_body": true}` |
| `image_config` | Dict[str, [components.ChatRequestImageConfig](../components/chatrequestimageconfig/index.md)] | ➖ | Provider-specific image configuration options. Keys and values vary by model/provider. See [https://openrouter.ai/docs/guides/overview/multimodal/image-generation](../../../../guides/overview/multimodal/image-generation/index.md) for more details. | `{"aspect_ratio": "16:9"}` |
| `modalities` | List[[components.Modality](../components/modality/index.md)] | ➖ | Output modalities for the response. Supported values are “text”, “image”, and “audio”. | [ “text”, “image” ] |
| `cache_control` | [Optional[components.AnthropicCacheControlDirective]](../../../components/anthropiccachecontroldirective.md/index.md) | ➖ | N/A | `{"type": "ephemeral"}` |
| `service_tier` | [OptionalNullable[components.ChatRequestServiceTier]](../../../components/chatrequestservicetier.md/index.md) | ➖ | The service tier to use for processing this request. | auto |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.SendChatCompletionRequestResponse](../operations/sendchatcompletionrequestresponse/index.md)**

### Errors

| Error Type | Status Code | Content Type |
| --- | --- | --- |
| errors.BadRequestResponseError | 400 | application/json |
| errors.UnauthorizedResponseError | 401 | application/json |
| errors.PaymentRequiredResponseError | 402 | application/json |
| errors.NotFoundResponseError | 404 | application/json |
| errors.RequestTimeoutResponseError | 408 | application/json |
| errors.PayloadTooLargeResponseError | 413 | application/json |
| errors.UnprocessableEntityResponseError | 422 | application/json |
| errors.TooManyRequestsResponseError | 429 | application/json |
| errors.InternalServerResponseError | 500 | application/json |
| errors.BadGatewayResponseError | 502 | application/json |
| errors.ServiceUnavailableResponseError | 503 | application/json |
| errors.EdgeNetworkTimeoutResponseError | 524 | application/json |
| errors.ProviderOverloadedResponseError | 529 | application/json |
| errors.OpenRouterDefaultError | 4XX, 5XX | \*/\* |
