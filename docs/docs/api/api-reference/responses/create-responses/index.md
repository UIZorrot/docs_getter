---
source_url: "https://openrouter.ai/docs/api/api-reference/responses/create-responses"
title: "Create a response | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:28.541173+00:00"
---
[API Reference](index.md)[Responses](index.md)

# Create a response

POST

https://openrouter.ai/api/v1/responses

POST

/api/v1/responses

```
|  |  |
| --- | --- |
| 1 | curl -X POST https://openrouter.ai/api/v1/responses \ |
| 2 | -H "Authorization: Bearer <token>" \ |
| 3 | -H "Content-Type: application/json" \ |
| 4 | -d '{ |
| 5 | "input": "Tell me a joke about computers", |
| 6 | "model": "openai/gpt-4o" |
| 7 | }' |
```

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "completed_at": 1700000010, |
| 3 | "created_at": 1700000000, |
| 4 | "error": { |
| 5 | "code": "rate_limit_exceeded", |
| 6 | "message": "Rate limit exceeded. Please try again later." |
| 7 | }, |
| 8 | "frequency_penalty": 0, |
| 9 | "id": "resp_abc123", |
| 10 | "incomplete_details": { |
| 11 | "reason": "max_output_tokens" |
| 12 | }, |
| 13 | "instructions": [ |
| 14 | { |
| 15 | "role": "user", |
| 16 | "content": "What is the weather today?" |
| 17 | } |
| 18 | ], |
| 19 | "metadata": { |
| 20 | "user_id": "user_12345", |
| 21 | "session_id": "session_abc123xyz" |
| 22 | }, |
| 23 | "model": "openai/gpt-4o", |
| 24 | "object": "response", |
| 25 | "parallel_tool_calls": true, |
| 26 | "presence_penalty": 0, |
| 27 | "status": "completed", |
| 28 | "temperature": 0.7, |
| 29 | "tool_choice": "auto", |
| 30 | "tools": [ |
| 31 | { |
| 32 | "type": "function", |
| 33 | "name": "get_weather", |
| 34 | "description": "Get the current weather in a location", |
| 35 | "parameters": { |
| 36 | "type": "object", |
| 37 | "properties": { |
| 38 | "location": { |
| 39 | "type": "string", |
| 40 | "description": "The city and state" |
| 41 | }, |
| 42 | "unit": { |
| 43 | "type": "string", |
| 44 | "enum": [ |
| 45 | "celsius", |
| 46 | "fahrenheit" |
| 47 | ] |
| 48 | } |
| 49 | }, |
| 50 | "required": [ |
| 51 | "location" |
| 52 | ] |
| 53 | } |
| 54 | } |
| 55 | ], |
| 56 | "top_p": 0.9, |
| 57 | "output": [ |
| 58 | { |
| 59 | "type": "message", |
| 60 | "status": "completed" |
| 61 | } |
| 62 | ], |
| 63 | "usage": { |
| 64 | "input_tokens": 15, |
| 65 | "input_tokens_details": { |
| 66 | "cached_tokens": 0 |
| 67 | }, |
| 68 | "output_tokens": 25, |
| 69 | "output_tokens_details": { |
| 70 | "reasoning_tokens": 5 |
| 71 | }, |
| 72 | "total_tokens": 40 |
| 73 | } |
| 74 | } |
```

Creates a streaming or non-streaming response using OpenResponses API format

### Authentication

AuthorizationBearer

API key as bearer token in Authorization header

### Request

This endpoint expects an object.

inputstring or list of objectsOptional

Input for a response request - can be a string or array of items

instructionsstring or nullOptional

metadatamap from strings to stringsOptional

Metadata key-value pairs for the request. Keys must be ≤64 characters and cannot contain brackets. Values must be ≤512 characters. Maximum 16 pairs allowed.

toolslist of objectsOptional

tool\_choiceenum or objectOptional

parallel\_tool\_callsboolean or nullOptional

modelstringOptional

modelslist of stringsOptional

textobjectOptional

Text output configuration including format and verbosity

reasoningobjectOptional

Configuration for reasoning mode in the response

max\_output\_tokensintegerOptional

temperaturedoubleOptional

top\_pdoubleOptional

top\_logprobsintegerOptional

max\_tool\_callsintegerOptional

presence\_penaltydoubleOptional

frequency\_penaltydoubleOptional

top\_kintegerOptional

image\_configmap from strings to strings or doublesOptional

Provider-specific image configuration options. Keys and values vary by model/provider. See [https://openrouter.ai/docs/features/multimodal/image-generation](../../../../features/multimodal/image-generation/index.md) for more details.

modalitieslist of enumsOptional

Output modalities for the response. Supported values are "text" and "image".

Allowed values:

prompt\_cache\_keystring or nullOptional

previous\_response\_idstring or nullOptional

promptobjectOptional

includelist of enums or nullOptional

Allowed values:

backgroundboolean or nullOptional

safety\_identifierstring or nullOptional

storefalseOptional

service\_tierenum or nullOptionalDefaults to `auto`

Allowed values:

truncationenumOptional

Allowed values:

streambooleanOptionalDefaults to `false`

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

### Response

Successful response

completed\_atinteger

created\_atinteger

errorobject

Error information returned from the API

frequency\_penaltydouble

idstring

incomplete\_detailsobject

instructionsstring or list of objects or any

metadatamap from strings to strings

Metadata key-value pairs for the request. Keys must be ≤64 characters and cannot contain brackets. Values must be ≤512 characters. Maximum 16 pairs allowed.

modelstring

objectenum

Allowed values:

parallel\_tool\_callsboolean

presence\_penaltydouble

statusenum

temperaturedouble

tool\_choiceenum or object

toolslist of objects

top\_pdouble

backgroundboolean or null

max\_output\_tokensinteger

max\_tool\_callsinteger

outputlist of objects

output\_textstring

previous\_response\_idstring or null

promptobject

prompt\_cache\_keystring or null

reasoningobject

safety\_identifierstring or null

service\_tierstring or null

storeboolean

textobject

Text output configuration including format and verbosity

top\_logprobsinteger

truncationenum

Allowed values:

usageobject

Token usage information for the response

userstring or null

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
