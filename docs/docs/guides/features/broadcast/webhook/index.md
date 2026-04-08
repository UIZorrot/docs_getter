---
source_url: "https://openrouter.ai/docs/guides/features/broadcast/webhook"
title: "Broadcast to Webhook | OpenRouter Observability | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:37.744237+00:00"
---
[Features](../../presets/index.md)[Broadcast](../overview/index.md)

# Webhook

Send traces to any HTTP endpoint

Webhook allows you to send traces to any HTTP endpoint that can receive JSON payloads. This is useful for integrating with custom observability systems, internal tools, or any service that accepts HTTP requests.

## Step 1: Set up your webhook endpoint

Create an HTTP endpoint that can receive POST or PUT requests with JSON payloads. Your endpoint should:

1. Accept `application/json` content type
2. Return a 2xx status code on success
3. Be publicly accessible from the internet

The endpoint will receive traces in [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp) format, making it compatible with any OTLP-aware system.

## Step 2: Enable Broadcast in OpenRouter

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

## Step 3: Configure Webhook

Click the edit icon next to **Webhook** and enter:

- **URL**: Your webhook endpoint URL (e.g., `https://api.example.com/traces`)
- **Method** (optional): HTTP method to use, either `POST` (default) or `PUT`
- **Headers** (optional): Custom HTTP headers as a JSON object for authentication or other purposes

Example headers for authenticated endpoints:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "Authorization": "Bearer your-token", |
| 3 | "X-Webhook-Signature": "your-webhook-secret" |
| 4 | } |
```

## Step 4: Test and save

Click **Test Connection** to verify the setup. The configuration only saves if the test passes. During the test, OpenRouter sends an empty OTLP payload with an `X-Test-Connection: true` header to your endpoint.

##### 

Your endpoint should return a 2xx status code for the test to pass. A 400 status code is also accepted, as some endpoints reject empty payloads.

## Step 5: Send a test trace

Make an API request through OpenRouter and verify that your webhook endpoint receives the trace data.

## Payload format

Traces are sent in OTLP JSON format. Each request contains a `resourceSpans` array with span data including:

- Trace and span IDs
- Timestamps and duration
- Model and provider information
- Token usage and cost
- Request and response content (with multimodal content stripped)

Example payload structure:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "resourceSpans": [ |
| 3 | { |
| 4 | "resource": { |
| 5 | "attributes": [ |
| 6 | { "key": "service.name", "value": { "stringValue": "openrouter" } } |
| 7 | ] |
| 8 | }, |
| 9 | "scopeSpans": [ |
| 10 | { |
| 11 | "spans": [ |
| 12 | { |
| 13 | "traceId": "abc123...", |
| 14 | "spanId": "def456...", |
| 15 | "name": "chat", |
| 16 | "startTimeUnixNano": "1705312800000000000", |
| 17 | "endTimeUnixNano": "1705312801000000000", |
| 18 | "attributes": [ |
| 19 | { "key": "gen_ai.request.model", "value": { "stringValue": "openai/gpt-4" } }, |
| 20 | { "key": "gen_ai.usage.prompt_tokens", "value": { "intValue": "100" } }, |
| 21 | { "key": "gen_ai.usage.completion_tokens", "value": { "intValue": "50" } } |
| 22 | ] |
| 23 | } |
| 24 | ] |
| 25 | } |
| 26 | ] |
| 27 | } |
| 28 | ] |
| 29 | } |
```

## Use cases

The Webhook destination is ideal for:

- **Custom analytics pipelines**: Send traces to your own data warehouse or analytics system
- **Internal monitoring tools**: Integrate with proprietary observability platforms
- **Event-driven architectures**: Trigger workflows based on LLM usage
- **Compliance logging**: Store traces in systems that meet specific regulatory requirements
- **Development and testing**: Use services like [webhook.site](https://webhook.site/) to inspect trace payloads

##### 

For production use, ensure your webhook endpoint is highly available and can handle the expected volume of traces. Consider implementing retry logic on your end for any failed deliveries.

## Custom Metadata

Custom metadata from the `trace` field is included as span attributes in the OTLP JSON payload sent to your webhook endpoint.

### Supported Metadata Keys

| Key | OTLP Mapping | Description |
| --- | --- | --- |
| `trace_id` | `traceId` | Group multiple requests into a single trace |
| `trace_name` | Span `name` | Custom name for the root span |
| `span_name` | Span `name` | Name for intermediate spans in the hierarchy |
| `generation_name` | Span `name` | Name for the LLM generation span |
| `parent_span_id` | `parentSpanId` | Link to an existing span in your trace hierarchy |

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Process this order..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_id": "order_processing_001", |
| 8 | "trace_name": "Order Processing Pipeline", |
| 9 | "generation_name": "Extract Order Details", |
| 10 | "order_id": "ORD-12345", |
| 11 | "priority": "high" |
| 12 | } |
| 13 | } |
```

### Accessing Metadata in Your Webhook

Custom metadata keys appear as span attributes in the OTLP payload under the `trace.metadata.*` namespace:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "resourceSpans": [{ |
| 3 | "scopeSpans": [{ |
| 4 | "spans": [{ |
| 5 | "attributes": [ |
| 6 | { "key": "trace.metadata.order_id", "value": { "stringValue": "ORD-12345" } }, |
| 7 | { "key": "trace.metadata.priority", "value": { "stringValue": "high" } } |
| 8 | ] |
| 9 | }] |
| 10 | }] |
| 11 | }] |
| 12 | } |
```

### Additional Context

- The `user` field maps to `user.id` in span attributes
- The `session_id` field maps to `session.id` in span attributes
- All standard GenAI semantic conventions (`gen_ai.*`) are included for model, token, and cost data

## Privacy Mode

When [Privacy Mode](../index.md) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](../index.md) for details.
