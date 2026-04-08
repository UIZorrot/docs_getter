---
source_url: "https://openrouter.ai/docs/api/api-reference/anthropic-messages/create-messages"
title: "Create a message | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:24.798416+00:00"
---
[API Reference](../../responses/create-responses/index.md)[Anthropic Messages](index.md)

# Create a message

POST

https://openrouter.ai/api/v1/messages

POST

/api/v1/messages

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/messages \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "model": "anthropic/claude-sonnet-4", |
| 6 | "messages": [ |
| 7 | { |
| 8 | "role": "user", |
| 9 | "content": "Hello, how are you?" |
| 10 | } |
| 11 | ], |
| 12 | "max_tokens": 1024 |
| 13 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "container": { |
| 3 | "id": "ctr_01abc", |
| 4 | "expires_at": "2026-04-08T00:00:00Z" |
| 5 | }, |
| 6 | "content": [ |
| 7 | { |
| 8 | "type": "text", |
| 9 | "text": "I'm doing well, thank you for asking! How can I help you today?", |
| 10 | "citations": [ |
| 11 | { |
| 12 | "type": "char_location", |
| 13 | "cited_text": "I'm doing well", |
| 14 | "document_index": 0, |
| 15 | "start_char_index": 0, |
| 16 | "end_char_index": 14 |
| 17 | } |
| 18 | ] |
| 19 | } |
| 20 | ], |
| 21 | "id": "msg_01XFDUDYJgAACzvnptvVoYEL", |
| 22 | "model": "anthropic/claude-sonnet-4", |
| 23 | "role": "assistant", |
| 24 | "stop_reason": "end_turn", |
| 25 | "stop_sequence": "\n", |
| 26 | "type": "message", |
| 27 | "usage": { |
| 28 | "cache_creation": { |
| 29 | "ephemeral_5m_input_tokens": 100, |
| 30 | "ephemeral_1h_input_tokens": 0 |
| 31 | }, |
| 32 | "cache_creation_input_tokens": 1, |
| 33 | "cache_read_input_tokens": 1, |
| 34 | "inference_geo": "us-west", |
| 35 | "input_tokens": 12, |
| 36 | "output_tokens": 18, |
| 37 | "server_tool_use": { |
| 38 | "web_search_requests": 1, |
| 39 | "web_fetch_requests": 0 |
| 40 | }, |
| 41 | "service_tier": "standard" |
| 42 | } |
| 43 | } |
```

Creates a message using the Anthropic Messages API format. Supports text, images, PDFs, tools, and extended thinking.

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

modelstringRequired

messageslist of objects or nullRequired

max\_tokensintegerOptional

systemstring or list of objectsOptional

metadataobjectOptional

stop\_sequenceslist of stringsOptional

temperaturedoubleOptional

top\_pdoubleOptional

top\_kintegerOptional

toolslist of objectsOptional

tool\_choiceobjectOptional

thinkingobjectOptional

service\_tierenumOptional

Allowed values:

output\_configobjectOptional

Configuration for controlling output behavior. Supports the effort parameter and structured output format.

cache\_controlobjectOptional

streambooleanOptional

context\_managementobject or nullOptional

providerobjectOptional

When multiple model providers are available, optionally indicate your routing preference.

pluginslist of objectsOptional

Plugins you want to enable for this request, including their settings.

routeanyOptional

userstringOptional`<=256 characters`

A unique identifier representing your end-user, which helps distinguish between different users of your app. This allows your app to identify specific users in case of abuse reports, preventing your entire app from being affected by the actions of individual users. Maximum of 256 characters.

session\_idstringOptional`<=256 characters`

A unique identifier for grouping related requests (e.g., a conversation or agent workflow) for observability. If provided in both the request body and the x-session-id header, the body value takes precedence. Maximum of 256 characters.

traceobjectOptional

Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations.

modelslist of stringsOptional

speedobjectOptional

### Response

Successful response

containerobject

contentlist of objects

idstring

modelstring

roleenum

Allowed values:

stop\_reasonenum

stop\_sequencestring or null

typeenum

Allowed values:

providerenum

usageobject

### Errors

400

Bad Request Error

401

Unauthorized Error

403

Forbidden Error

404

Not Found Error

429

Too Many Requests Error

500

Internal Server Error

503

Service Unavailable Error
