---
source_url: "https://openrouter.ai/docs/api/api-reference/chat/send-chat-completion-request"
title: "Create a chat completion | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:58.345920+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Chat](index.md)

# Create a chat completion

POST

https://openrouter.ai/api/v1/chat/completions

POST

/api/v1/chat/completions

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/chat/completions \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "messages": [ |
| 6 | { |
| 7 | "role": "system", |
| 8 | "content": "You are a helpful assistant." |
| 9 | }, |
| 10 | { |
| 11 | "role": "user", |
| 12 | "content": "What is the capital of France?" |
| 13 | } |
| 14 | ], |
| 15 | "model": "openai/gpt-4", |
| 16 | "max_tokens": 150, |
| 17 | "temperature": 0.7 |
| 18 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "id": "chatcmpl-123", |
| 3 | "choices": [ |
| 4 | { |
| 5 | "finish_reason": "stop", |
| 6 | "index": 0, |
| 7 | "message": { |
| 8 | "role": "assistant", |
| 9 | "content": "The capital of France is Paris." |
| 10 | } |
| 11 | } |
| 12 | ], |
| 13 | "created": 1677652288, |
| 14 | "model": "openai/gpt-4", |
| 15 | "object": "chat.completion", |
| 16 | "system_fingerprint": "fp_44709d6fcb", |
| 17 | "usage": { |
| 18 | "completion_tokens": 10, |
| 19 | "prompt_tokens": 25, |
| 20 | "total_tokens": 35 |
| 21 | } |
| 22 | } |
```

Sends a request for a model response for the given chat conversation. Supports both streaming and non-streaming modes.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

messageslist of objectsRequired

List of messages for the conversation

providerobjectOptional

When multiple model providers are available, optionally indicate your routing preference.

pluginslist of objectsOptional

Plugins you want to enable for this request, including their settings.

routeanyOptional

userstringOptional

Unique user identifier

session\_idstringOptional`<=256 characters`

A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 256 characters.

traceobjectOptional

Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations.

modelstringOptional

Model to use for completion

modelslist of objectsOptional

Models to use for completion

frequency\_penaltydoubleOptional

Frequency penalty (-2.0 to 2.0)

logit\_biasmap from strings to doubles or nullOptional

Token logit bias adjustments

logprobsboolean or nullOptional

Return log probabilities

top\_logprobsintegerOptional

Number of top log probabilities to return (0-20)

max\_completion\_tokensintegerOptional

Maximum tokens in completion

max\_tokensintegerOptional

Maximum tokens (deprecated, use max\_completion\_tokens). Note: some providers enforce a minimum of 16.

metadatamap from strings to stringsOptional

Key-value pairs for additional object information (max 16 pairs, 64 char keys, 512 char values)

presence\_penaltydoubleOptional

Presence penalty (-2.0 to 2.0)

reasoningobjectOptional

Configuration options for reasoning models

response\_formatobjectOptional

Response format configuration

seedintegerOptional

Random seed for deterministic outputs

stopstring or list of strings or anyOptional

Stop sequences (up to 4)

streambooleanOptionalDefaults to `false`

Enable streaming response

stream\_optionsobjectOptional

Streaming configuration options

temperaturedoubleOptional

Sampling temperature (0-2)

parallel\_tool\_callsboolean or nullOptional

Whether to enable parallel function calling during tool use. When true, the model may generate multiple tool calls in a single response.

tool\_choiceenum or objectOptional

Tool choice configuration

toolslist of objectsOptional

Available tools for function calling

top\_pdoubleOptional

Nucleus sampling parameter (0-1)

debugobjectOptional

Debug options for inspecting request transformations (streaming only)

image\_configmap from strings to strings or doubles or lists of anyOptional

Provider-specific image configuration options. Keys and values vary by model/provider. See [https://openrouter.ai/docs/guides/overview/multimodal/image-generation](../../../../guides/overview/multimodal/image-generation/index.md) for more details.

modalitieslist of enumsOptional

Output modalities for the response. Supported values are "text", "image", and "audio".

Allowed values:

cache\_controlobjectOptional

service\_tierenum or nullOptional

The service tier to use for processing this request.

Allowed values:

### Response

Successful chat completion response

idstring

Unique completion identifier

choiceslist of objects

List of completion choices

createdinteger

Unix timestamp of creation

modelstring

Model used for completion

objectenum

Allowed values:

system\_fingerprintstring or null

System fingerprint

service\_tierstring or null

The service tier used by the upstream provider for this request

usageobject

Token usage statistics

### Errors

400

Bad Request Error

401

Unauthorized Error

402

Payment Required Error

404

Not Found Error

408

Request Timeout Error

413

Content Too Large Error

422

Unprocessable Entity Error

429

Too Many Requests Error

500

Internal Server Error

502

Bad Gateway Error

503

Service Unavailable Error
