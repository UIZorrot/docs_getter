---
source_url: "https://openrouter.ai/docs/api/reference/errors-and-debugging"
title: "API Error Handling and Debugging | OpenRouter Documentation | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:29.095636+00:00"
---
[API Guides](../overview/index.md)

# Errors and Debugging

API Errors and Debugging

For errors, OpenRouter returns a JSON response with the following shape:

```
|  |  |
| --- | --- |
| 1 | type ErrorResponse = { |
| 2 | error: { |
| 3 | code: number; |
| 4 | message: string; |
| 5 | metadata?: Record<string, unknown>; |
| 6 | }; |
| 7 | }; |
```

The HTTP Response will have the same status code as `error.code`, forming a request error if:

- Your original request is invalid
- Your API key/account is out of credits

Otherwise, the returned HTTP response status will be `200` and any error occurred while the LLM is producing the output will be emitted in the response body or as an SSE data event.

Example code for printing errors in JavaScript:

```
|  |  |
| --- | --- |
| 1 | const request = await fetch('https://openrouter.ai/...'); |
| 2 | console.log(request.status); // Will be an error code unless the model started processing your request |
| 3 | const response = await request.json(); |
| 4 | console.error(response.error?.status); // Will be an error code |
| 5 | console.error(response.error?.message); |
```

## Error Codes

- **400**: Bad Request (invalid or missing params, CORS)
- **401**: Invalid credentials (OAuth session expired, disabled/invalid API key)
- **402**: Your account or API key has insufficient credits. Add more credits and retry the request.
- **403**: Your chosen model requires moderation and your input was flagged
- **408**: Your request timed out
- **429**: You are being rate limited
- **502**: Your chosen model is down or we received an invalid response from it
- **503**: There is no available model provider that meets your routing requirements

## Moderation Errors

If your input was flagged, the `error.metadata` will contain information about the issue. The shape of the metadata is as follows:

```
|  |  |
| --- | --- |
| 1 | type ModerationErrorMetadata = { |
| 2 | reasons: string[]; // Why your input was flagged |
| 3 | flagged_input: string; // The text segment that was flagged, limited to 100 characters. If the flagged input is longer than 100 characters, it will be truncated in the middle and replaced with ... |
| 4 | provider_name: string; // The name of the provider that requested moderation |
| 5 | model_slug: string; |
| 6 | }; |
```

## Provider Errors

If the model provider encounters an error, the `error.metadata` will contain information about the issue. The shape of the metadata is as follows:

```
|  |  |
| --- | --- |
| 1 | type ProviderErrorMetadata = { |
| 2 | provider_name: string; // The name of the provider that encountered the error |
| 3 | raw: unknown; // The raw error from the provider |
| 4 | }; |
```

## When No Content is Generated

Occasionally, the model may not generate any content. This typically occurs when:

- The model is warming up from a cold start
- The system is scaling up to handle more requests

Warm-up times usually range from a few seconds to a few minutes, depending on the model and provider.

If you encounter persistent no-content issues, consider implementing a simple retry mechanism or trying again with a different provider or model that has more recent activity.

Additionally, be aware that in some cases, you may still be charged for the prompt processing cost by the upstream provider, even if no content is generated.

## Streaming Error Formats

When using streaming mode (`stream: true`), errors are handled differently depending on when they occur:

### Pre-Stream Errors

Errors that occur before any tokens are sent follow the standard error format above, with appropriate HTTP status codes.

### Mid-Stream Errors

Errors that occur after streaming has begun are sent as Server-Sent Events (SSE) with a unified structure that includes both the error details and a completion choice:

```
|  |  |
| --- | --- |
| 1 | type MidStreamError = { |
| 2 | id: string; |
| 3 | object: 'chat.completion.chunk'; |
| 4 | created: number; |
| 5 | model: string; |
| 6 | provider: string; |
| 7 | error: { |
| 8 | code: string | number; |
| 9 | message: string; |
| 10 | }; |
| 11 | choices: [{ |
| 12 | index: 0; |
| 13 | delta: { content: '' }; |
| 14 | finish_reason: 'error'; |
| 15 | native_finish_reason?: string; |
| 16 | }]; |
| 17 | }; |
```

Example SSE data:

```
|  |
| --- |
| data: {"id":"cmpl-abc123","object":"chat.completion.chunk","created":1234567890,"model":"gpt-3.5-turbo","provider":"openai","error":{"code":"server_error","message":"Provider disconnected"},"choices":[{"index":0,"delta":{"content":""},"finish_reason":"error"}]} |
```

Key characteristics:

- The error appears at the **top level** alongside standard response fields
- A `choices` array is included with `finish_reason: "error"` to properly terminate the stream
- The HTTP status remains 200 OK since headers were already sent
- The stream is terminated after this event

## OpenAI Responses API Error Events

The OpenAI Responses API (`/api/alpha/responses`) uses specific event types for streaming errors:

### Error Event Types

1. **`response.failed`** - Official failure event

   ```
   |  |  |
   | --- | --- |
   | 1 | { |
   | 2 | "type": "response.failed", |
   | 3 | "response": { |
   | 4 | "id": "resp_abc123", |
   | 5 | "status": "failed", |
   | 6 | "error": { |
   | 7 | "code": "server_error", |
   | 8 | "message": "Internal server error" |
   | 9 | } |
   | 10 | } |
   | 11 | } |
   ```
2. **`response.error`** - Error during response generation

   ```
   |  |  |
   | --- | --- |
   | 1 | { |
   | 2 | "type": "response.error", |
   | 3 | "error": { |
   | 4 | "code": "rate_limit_exceeded", |
   | 5 | "message": "Rate limit exceeded" |
   | 6 | } |
   | 7 | } |
   ```
3. **`error`** - Plain error event (undocumented but sent by OpenAI)

   ```
   |  |  |
   | --- | --- |
   | 1 | { |
   | 2 | "type": "error", |
   | 3 | "error": { |
   | 4 | "code": "invalid_api_key", |
   | 5 | "message": "Invalid API key provided" |
   | 6 | } |
   | 7 | } |
   ```

### Error Code Transformations

The Responses API transforms certain error codes into successful completions with specific finish reasons:

| Error Code | Transformed To | Finish Reason |
| --- | --- | --- |
| `context_length_exceeded` | Success | `length` |
| `max_tokens_exceeded` | Success | `length` |
| `token_limit_exceeded` | Success | `length` |
| `string_too_long` | Success | `length` |

This allows for graceful handling of limit-based errors without treating them as failures.

## API-Specific Error Handling

Different OpenRouter API endpoints handle errors in distinct ways:

### OpenAI Chat Completions API (`/api/v1/chat/completions`)

- **No tokens sent**: Returns standalone `ErrorResponse`
- **Some tokens sent**: Embeds error information within the `choices` array of the final response
- **Streaming**: Errors sent as SSE events with top-level error field

### OpenAI Responses API (`/api/alpha/responses`)

- **Error transformations**: Certain errors become successful responses with appropriate finish reasons
- **Streaming events**: Uses typed events (`response.failed`, `response.error`, `error`)
- **Graceful degradation**: Handles provider-specific errors with fallback behavior

### Error Response Type Definitions

```
|  |  |
| --- | --- |
| 1 | // Standard error response |
| 2 | interface ErrorResponse { |
| 3 | error: { |
| 4 | code: number; |
| 5 | message: string; |
| 6 | metadata?: Record<string, unknown>; |
| 7 | }; |
| 8 | } |
| 9 |  |
| 10 | // Mid-stream error with completion data |
| 11 | interface StreamErrorChunk { |
| 12 | error: { |
| 13 | code: string | number; |
| 14 | message: string; |
| 15 | }; |
| 16 | choices: Array<{ |
| 17 | delta: { content: string }; |
| 18 | finish_reason: 'error'; |
| 19 | native_finish_reason: string; |
| 20 | }>; |
| 21 | } |
| 22 |  |
| 23 | // Responses API error event |
| 24 | interface ResponsesAPIErrorEvent { |
| 25 | type: 'response.failed' | 'response.error' | 'error'; |
| 26 | error?: { |
| 27 | code: string; |
| 28 | message: string; |
| 29 | }; |
| 30 | response?: { |
| 31 | id: string; |
| 32 | status: 'failed'; |
| 33 | error: { |
| 34 | code: string; |
| 35 | message: string; |
| 36 | }; |
| 37 | }; |
| 38 | } |
```

## Debugging

OpenRouter provides a `debug` option that allows you to inspect the exact request body that was sent to the upstream provider. This is useful for understanding how OpenRouter transforms your request parameters to work with different providers.

### Debug Option Shape

The debug option is an object with the following shape:

```
|  |  |
| --- | --- |
| 1 | type DebugOptions = { |
| 2 | echo_upstream_body?: boolean; // If true, returns the transformed request body sent to the provider |
| 3 | }; |
```

### Usage

To enable debug output, include the `debug` parameter in your request:

```
|  |  |
| --- | --- |
| 1 | fetch('https://openrouter.ai/api/v1/chat/completions', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | Authorization: 'Bearer <OPENROUTER_API_KEY>', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: 'anthropic/claude-haiku-4.5', |
| 9 | stream: true, // Debug only works with streaming |
| 10 | messages: [ |
| 11 | { role: 'system', content: 'You are a helpful assistant.' }, |
| 12 | { role: 'user', content: 'Hello!' }, |
| 13 | ], |
| 14 | debug: { |
| 15 | echo_upstream_body: true, |
| 16 | }, |
| 17 | }), |
| 18 | }); |
| 19 |  |
| 20 | const text = await response.text(); |
| 21 |  |
| 22 | for (const line of text.split('\n')) { |
| 23 | if (!line.startsWith('data: ')) continue; |
| 24 |  |
| 25 | const data = line.slice(6); |
| 26 | if (data === '[DONE]') break; |
| 27 |  |
| 28 | const parsed = JSON.parse(data); |
| 29 |  |
| 30 | if (parsed.debug?.echo_upstream_body) { |
| 31 | console.log('\nDebug:', JSON.stringify(parsed.debug.echo_upstream_body, null, 2)); |
| 32 | } |
| 33 |  |
| 34 | process.stdout.write(parsed.choices?.[0]?.delta?.content ?? ''); |
| 35 | } |
```

### Debug Response Format

When `debug.echo_upstream_body` is set to `true`, OpenRouter will send a debug chunk as the **first chunk** in the streaming response. This chunk will have an empty `choices` array and include a `debug` field containing the transformed request body:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "id": "gen-xxxxx", |
| 3 | "provider": "Anthropic", |
| 4 | "model": "anthropic/claude-haiku-4.5", |
| 5 | "object": "chat.completion.chunk", |
| 6 | "created": 1234567890, |
| 7 | "choices": [], |
| 8 | "debug": { |
| 9 | "echo_upstream_body": { |
| 10 | "system": [ |
| 11 | { "type": "text", "text": "You are a helpful assistant." } |
| 12 | ], |
| 13 | "messages": [ |
| 14 | { "role": "user", "content": "Hello!" } |
| 15 | ], |
| 16 | "model": "claude-haiku-4-5-20251001", |
| 17 | "stream": true, |
| 18 | "max_tokens": 64000, |
| 19 | "temperature": 1 |
| 20 | } |
| 21 | } |
| 22 | } |
```

### Important Notes

##### Streaming Chat Completions Only

The debug option **only works with streaming mode** (`stream: true`) for the Chat Completions API. Non-streaming requests and Responses API requests will ignore the debug parameter.

##### Not for Production

The debug flag should **not be used in production environments**. It is intended for development and debugging purposes only, as it may potentially return sensitive information included in the request that was not intended to be visible elsewhere.

### Use Cases

The debug output is particularly useful for:

1. **Understanding Parameter Transformations**: See how OpenRouter maps your parameters to provider-specific formats (e.g., how `max_tokens` is set, how `temperature` is handled).
2. **Verifying Message Formatting**: Check how OpenRouter combines and formats your messages for different providers (e.g., how system messages are concatenated, how user messages are merged).
3. **Checking Applied Defaults**: See what default values OpenRouter applies when parameters are not specified in your request.
4. **Debugging Provider Fallbacks**: When using provider fallbacks, a debug chunk will be sent for **each attempted provider**, allowing you to see which providers were tried and what parameters were sent to each.

### Privacy and Redaction

OpenRouter will make a best effort to automatically redact potentially sensitive or noisy data from debug output. Remember that the debug option is not intended for production.
