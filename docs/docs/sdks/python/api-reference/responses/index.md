---
source_url: "https://openrouter.ai/docs/sdks/python/api-reference/responses"
title: "Beta.Responses | OpenRouter Python SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:45.010219+00:00"
---
[Python SDK](../../overview/index.md)[API Reference](../analytics/index.md)

# 

Beta.Responses - Python SDK

Beta.Responses method reference

##### 

The Python SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/python-sdk/issues).

## Overview

beta.responses endpoints

### Available Operations

- [send](#send) - Create a response

## send

Creates a streaming or non-streaming response using OpenResponses API format

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
| 11 | res = open_router.beta.responses.send(input="Tell me a joke", model="openai/gpt-4o", service_tier="auto", stream=False) |
| 12 |  |
| 13 | with res as event_stream: |
| 14 | for event in event_stream: |
| 15 | # handle event |
| 16 | print(event, flush=True) |
```

### Parameters

| Parameter | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `http_referer` | *Optional[str]* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `x_open_router_title` | *Optional[str]* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `x_open_router_categories` | *Optional[str]* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `input` | [Optional[components.InputsUnion]](../../../components/inputsunion.md/index.md) | ➖ | Input for a response request - can be a string or array of items | [ `{"role": "user","content": "What is the weather today?"}` ] |
| `instructions` | *OptionalNullable[str]* | ➖ | N/A |  |
| `metadata` | Dict[str, *str*] | ➖ | Metadata key-value pairs for the request. Keys must be ≤64 characters and cannot contain brackets. Values must be ≤512 characters. Maximum 16 pairs allowed. | `{"user_id": "123","session_id": "abc-def-ghi"}` |
| `tools` | List[[components.ResponsesRequestToolUnion](../components/responsesrequesttoolunion/index.md)] | ➖ | N/A |  |
| `tool_choice` | [Optional[components.OpenAIResponsesToolChoiceUnion]](../../../components/openairesponsestoolchoiceunion.md/index.md) | ➖ | N/A | auto |
| `parallel_tool_calls` | *OptionalNullable[bool]* | ➖ | N/A |  |
| `model` | *Optional[str]* | ➖ | N/A |  |
| `models` | List[*str*] | ➖ | N/A |  |
| `text` | [Optional[components.TextExtendedConfig]](../../../components/textextendedconfig.md/index.md) | ➖ | Text output configuration including format and verbosity | `{"format": {"type": "text"}`, “verbosity”: “medium” } |
| `reasoning` | [OptionalNullable[components.ReasoningConfig]](../../../components/reasoningconfig.md/index.md) | ➖ | Configuration for reasoning mode in the response | `{"effort": "medium","summary": "auto"}` |
| `max_output_tokens` | *Optional[int]* | ➖ | N/A |  |
| `temperature` | *Optional[float]* | ➖ | N/A |  |
| `top_p` | *Optional[float]* | ➖ | N/A |  |
| `top_logprobs` | *Optional[int]* | ➖ | N/A |  |
| `max_tool_calls` | *Optional[int]* | ➖ | N/A |  |
| `presence_penalty` | *Optional[float]* | ➖ | N/A |  |
| `frequency_penalty` | *Optional[float]* | ➖ | N/A |  |
| `top_k` | *Optional[int]* | ➖ | N/A |  |
| `image_config` | Dict[str, [components.ResponsesRequestImageConfig](../components/responsesrequestimageconfig/index.md)] | ➖ | Provider-specific image configuration options. Keys and values vary by model/provider. See [https://openrouter.ai/docs/features/multimodal/image-generation](../../../../features/multimodal/image-generation/index.md) for more details. | `{"aspect_ratio": "16:9"}` |
| `modalities` | List[[components.OutputModalityEnum](../components/outputmodalityenum/index.md)] | ➖ | Output modalities for the response. Supported values are “text” and “image”. | [ “text”, “image” ] |
| `prompt_cache_key` | *OptionalNullable[str]* | ➖ | N/A |  |
| `previous_response_id` | *OptionalNullable[str]* | ➖ | N/A |  |
| `prompt` | [OptionalNullable[components.StoredPromptTemplate]](../../../components/storedprompttemplate.md/index.md) | ➖ | N/A | `{"id": "prompt-abc123","variables": {"name": "John"}` } |
| `include` | List[[components.ResponseIncludesEnum](../components/responseincludesenum/index.md)] | ➖ | N/A |  |
| `background` | *OptionalNullable[bool]* | ➖ | N/A |  |
| `safety_identifier` | *OptionalNullable[str]* | ➖ | N/A |  |
| `service_tier` | [OptionalNullable[components.ResponsesRequestServiceTier]](../../../components/responsesrequestservicetier.md/index.md) | ➖ | N/A |  |
| `truncation` | [OptionalNullable[components.OpenAIResponsesTruncation]](../../../components/openairesponsestruncation.md/index.md) | ➖ | N/A | auto |
| `stream` | *Optional[bool]* | ➖ | N/A |  |
| `provider` | [OptionalNullable[components.ProviderPreferences]](../../../components/providerpreferences.md/index.md) | ➖ | When multiple model providers are available, optionally indicate your routing preference. | `{"allow_fallbacks": true}` |
| `plugins` | List[[components.ResponsesRequestPlugin](../components/responsesrequestplugin/index.md)] | ➖ | Plugins you want to enable for this request, including their settings. |  |
| `user` | *Optional[str]* | ➖ | A unique identifier representing your end-user, which helps distinguish between different users of your app. This allows your app to identify specific users in case of abuse reports, preventing your entire app from being affected by the actions of individual users. Maximum of 256 characters. |  |
| `session_id` | *Optional[str]* | ➖ | A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 256 characters. |  |
| `trace` | [Optional[components.TraceConfig]](../../../components/traceconfig.md/index.md) | ➖ | Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations. | `{"trace_id": "trace-abc123","trace_name": "my-app-trace"}` |
| `retries` | [Optional[utils.RetryConfig]](../../../models/utils/retryconfig.md/index.md) | ➖ | Configuration to override the default retry behavior of the client. |  |

### Response

**[operations.CreateResponsesResponse](../operations/createresponsesresponse/index.md)**

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
