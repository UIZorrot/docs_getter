---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/responsesrequest"
title: "ResponsesRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.454518+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ResponsesRequest - TypeScript SDK

ResponsesRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Request schema for Responses endpoint

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ResponsesRequest } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ResponsesRequest = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `input` | *models.InputsUnion* | ➖ | Input for a response request - can be a string or array of items | [ `{"role": "user","content": "What is the weather today?"}` ] |
| `instructions` | *string* | ➖ | N/A |  |
| `metadata` | `Record<string, *string*>` | ➖ | Metadata key-value pairs for the request. Keys must be ≤64 characters and cannot contain brackets. Values must be ≤512 characters. Maximum 16 pairs allowed. | `{"user_id": "123","session_id": "abc-def-ghi"}` |
| `tools` | *models.ResponsesRequestToolUnion*[] | ➖ | N/A |  |
| `toolChoice` | *models.OpenAIResponsesToolChoiceUnion* | ➖ | N/A | auto |
| `parallelToolCalls` | *boolean* | ➖ | N/A |  |
| `model` | *string* | ➖ | N/A |  |
| `models` | *string*[] | ➖ | N/A |  |
| `text` | [models.TextExtendedConfig](../textextendedconfig/index.md) | ➖ | Text output configuration including format and verbosity | `{"format": {"type": "text"}` } |
| `reasoning` | [models.ReasoningConfig](../reasoningconfig/index.md) | ➖ | Configuration for reasoning mode in the response | `{"summary": "auto","enabled": true}` |
| `maxOutputTokens` | *number* | ➖ | N/A |  |
| `temperature` | *number* | ➖ | N/A |  |
| `topP` | *number* | ➖ | N/A |  |
| `topLogprobs` | *number* | ➖ | N/A |  |
| `maxToolCalls` | *number* | ➖ | N/A |  |
| `presencePenalty` | *number* | ➖ | N/A |  |
| `frequencyPenalty` | *number* | ➖ | N/A |  |
| `topK` | *number* | ➖ | N/A |  |
| `imageConfig` | `Record<string, *models.ResponsesRequestImageConfig*>` | ➖ | Provider-specific image configuration options. Keys and values vary by model/provider. See [https://openrouter.ai/docs/features/multimodal/image-generation](../../../../../features/multimodal/image-generation/index.md) for more details. | `{"aspect_ratio": "16:9"}` |
| `modalities` | [models.OutputModalityEnum](../outputmodalityenum/index.md)[] | ➖ | Output modalities for the response. Supported values are “text” and “image”. | [ “text”, “image” ] |
| `promptCacheKey` | *string* | ➖ | N/A |  |
| `previousResponseId` | *string* | ➖ | N/A |  |
| `prompt` | [models.StoredPromptTemplate](../storedprompttemplate/index.md) | ➖ | N/A | `{"id": "prompt-abc123","variables": {"name": "John"}` } |
| `include` | [models.ResponseIncludesEnum](../responseincludesenum/index.md)[] | ➖ | N/A |  |
| `background` | *boolean* | ➖ | N/A |  |
| `safetyIdentifier` | *string* | ➖ | N/A |  |
| `store` | *false* | ➖ | N/A |  |
| `serviceTier` | [models.ResponsesRequestServiceTier](../responsesrequestservicetier/index.md) | ➖ | N/A |  |
| `truncation` | [models.OpenAIResponsesTruncation](../openairesponsestruncation/index.md) | ➖ | N/A | auto |
| `stream` | *boolean* | ➖ | N/A |  |
| `provider` | [models.ProviderPreferences](../providerpreferences/index.md) | ➖ | When multiple model providers are available, optionally indicate your routing preference. | `{"allow_fallbacks": true}` |
| `plugins` | *models.ResponsesRequestPlugin*[] | ➖ | Plugins you want to enable for this request, including their settings. |  |
| `user` | *string* | ➖ | A unique identifier representing your end-user, which helps distinguish between different users of your app. This allows your app to identify specific users in case of abuse reports, preventing your entire app from being affected by the actions of individual users. Maximum of 256 characters. |  |
| `sessionId` | *string* | ➖ | A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 256 characters. |  |
| `trace` | [models.TraceConfig](../traceconfig/index.md) | ➖ | Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations. | `{"trace_id": "trace-abc123","trace_name": "my-app-trace"}` |
