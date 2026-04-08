---
source_url: "https://openrouter.ai/docs/guides/features/broadcast/overview"
title: "Broadcast | OpenRouter Observability | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:56.139075+00:00"
---
[Features](../../presets/index.md)[Broadcast](index.md)

# Broadcast

Send traces to external observability platforms

Broadcast allows you to automatically send traces from your OpenRouter requests to external observability and analytics platforms. This feature enables you to monitor, debug, and analyze your LLM usage across your preferred tools without any additional instrumentation in your application code.

## Enabling Broadcast

To enable broadcast for your account or organization:

1. Navigate to [Settings > Observability](https://openrouter.ai/settings/observability) in your OpenRouter dashboard
2. Toggle the “Enable Broadcast” switch to turn on the feature
3. Add one or more destinations where you want to send your traces

##### 

If you’re using an organization account, you must be an organization admin to edit broadcast settings.

Once enabled, OpenRouter will automatically send trace data for all your API requests to your configured destinations.

## Supported Destinations

The following destinations are currently available:

- [Arize AI](../arize/index.md)
- [Braintrust](../braintrust/index.md)
- [ClickHouse](../clickhouse/index.md)
- [Comet Opik](../opik/index.md)
- [Datadog](../datadog/index.md)
- [Grafana Cloud](../grafana/index.md)
- [Langfuse](../langfuse/index.md)
- [LangSmith](../langsmith/index.md)
- [New Relic](../newrelic/index.md)
- [OpenTelemetry Collector](../otel-collector/index.md)
- [PostHog](../posthog/index.md)
- [S3 / S3-Compatible](../s3/index.md)
- [Sentry](../sentry/index.md)
- [Snowflake](../snowflake/index.md)
- [W&B Weave](../weave/index.md)
- [Webhook](../webhook/index.md)

Each destination has its own configuration requirements, such as API keys, endpoints, or project identifiers. When adding a destination, you’ll be prompted to provide the necessary credentials which are encrypted and stored securely.

For the most up-to-date list of available destinations, visit the [Broadcast settings page](https://openrouter.ai/settings/observability) in your dashboard.

### Coming Soon

The following destinations are in development and will be available soon:

- AWS Firehose
- Dynatrace
- Evidently
- Fiddler
- Galileo
- Helicone
- HoneyHive
- Keywords AI
- Middleware
- Mona
- OpenInference
- Phoenix
- Portkey
- Supabase
- WhyLabs

## Trace Data

Each broadcast trace includes comprehensive information about your API request:

- **Request & Response Data**: The input messages and model output (with multimodal content stripped for efficiency)
- **Token Usage**: Prompt tokens, completion tokens, and total tokens consumed
- **Cost Information**: The total cost of the request
- **Timing**: Request start time, end time, and latency metrics
- **Model Information**: The model slug and provider name used for the request
- **Tool Usage**: Whether tools were included in the request and if tool calls were made

### Optional Trace Data

You can enrich your traces with additional context by including these optional fields in your API requests:

- **User ID**: Associate traces with specific end-users by including the `user` field (up to 128 characters). This helps you track usage patterns and debug issues for individual users.

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [ |
| 4 | { |
| 5 | "role": "user", |
| 6 | "content": "Hello, world!" |
| 7 | } |
| 8 | ], |
| 9 | "user": "user_12345" |
| 10 | } |
```

- **Session ID**: Group related requests together (such as a conversation or agent workflow) by including the `session_id` field (up to 128 characters). You can also pass this via the `x-session-id` HTTP header.

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [ |
| 4 | { |
| 5 | "role": "user", |
| 6 | "content": "Hello, world!" |
| 7 | } |
| 8 | ], |
| 9 | "session_id": "session_abc123" |
| 10 | } |
```

### Custom Metadata

For advanced observability workflows, you can pass arbitrary metadata to your traces using the `trace` field. This field accepts any JSON object and is passed through to all your configured broadcast destinations.

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [ |
| 4 | { |
| 5 | "role": "user", |
| 6 | "content": "Summarize this document..." |
| 7 | } |
| 8 | ], |
| 9 | "trace": { |
| 10 | "trace_id": "workflow_12345", |
| 11 | "trace_name": "Document Processing", |
| 12 | "span_name": "Summarization Step", |
| 13 | "generation_name": "Generate Summary", |
| 14 | "environment": "production", |
| 15 | "feature": "customer-support", |
| 16 | "version": "1.2.3" |
| 17 | } |
| 18 | } |
```

##### 

The `trace` field is flexible and accepts any key-value pairs. Certain keys have special meaning depending on your observability destination. See the destination-specific documentation for details on which keys each platform recognizes.

#### Common Metadata Keys

These metadata keys are commonly used across observability platforms:

| Key | Description |
| --- | --- |
| `trace_id` | Group multiple API requests into a single trace. Use the same ID across requests to track multi-step workflows. |
| `trace_name` | Custom name for the root trace in your observability platform. Defaults to the model name if not set. |
| `span_name` | Create a parent span that groups LLM operations. Creates hierarchical structure where the span contains the generation. |
| `generation_name` | Custom name for the specific LLM generation/call. Defaults to the model name if not set. |
| `parent_span_id` | Link your OpenRouter trace to an existing span from your own tracing system (e.g., OpenTelemetry). |

When using these fields, your traces will appear with a hierarchical structure in platforms like Langfuse:

```
|  |
| --- |
| Document Processing (trace_id: workflow_12345) |
| └── Summarization Step (span) |
| └── Generate Summary (generation) |
```

#### Linking to External Traces

If you have your own tracing instrumentation (e.g., OpenTelemetry), you can use `parent_span_id` to nest OpenRouter calls under your existing spans:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Hello!" }], |
| 4 | "trace": { |
| 5 | "trace_id": "your-existing-trace-id", |
| 6 | "parent_span_id": "your-existing-span-id" |
| 7 | } |
| 8 | } |
```

This will create a trace structure like:

```
|  |
| --- |
| Your Application Trace |
| └── Your Application Span (parent_span_id) |
| └── openai/gpt-4o (generation from OpenRouter) |
```

This enables you to:

- Track end-to-end workflows spanning multiple LLM calls
- Organize traces by business logic rather than individual API calls
- Build rich observability dashboards with meaningful trace names
- Integrate OpenRouter traces with your existing application traces
- Pass any custom data you need to your observability platforms

#### Destination-Specific Metadata

Each observability platform may recognize different metadata keys. See the destination-specific guides for details:

- [Langfuse](../langfuse/index.md) - Supports trace naming, user/session IDs, and arbitrary metadata
- [LangSmith](../langsmith/index.md) - Supports tags, session tracking, and metadata
- [Datadog](../datadog/index.md) - Supports tags, user IDs, and session IDs
- [Braintrust](../braintrust/index.md) - Supports tags and custom metadata fields
- [W&B Weave](../weave/index.md) - Supports custom attributes in trace data
- [Arize AI](../arize/index.md) - Supports OpenInference span attributes and metadata
- [Comet Opik](../opik/index.md) - Supports trace/span metadata and cost tracking
- [Grafana Cloud](../grafana/index.md) - Supports TraceQL-queryable span attributes
- [New Relic](../newrelic/index.md) - Supports NRQL-queryable span attributes
- [Sentry](../sentry/index.md) - Supports span attributes for performance monitoring
- [OpenTelemetry Collector](../otel-collector/index.md) - Supports OTLP span attributes for any backend
- [Webhook](../webhook/index.md) - Custom metadata in OTLP JSON payload
- [PostHog](../posthog/index.md) - Supports event properties for LLM analytics
- [Snowflake](../snowflake/index.md) - Queryable via VARIANT column functions
- [ClickHouse](../clickhouse/index.md) - Queryable via JSONExtract functions
- [S3](../s3/index.md) - Stored in trace JSON files

## API Key Filtering

Each destination can be configured to only receive traces from specific API keys. This is useful when you want to:

- route traces from different parts of your application to different observability platforms
- isolate monitoring for specific use cases
- or send production API key traces at a lower sampling rate than development keys

When adding or editing a destination, you can select one or more API keys from your account. Only requests made with those selected API keys will have their traces sent to that destination. If no API keys are selected, the destination will receive traces from all your API keys or chatroom requests.

## Sampling Rate

Each destination can be configured with a sampling rate to control what percentage of traces are sent. This is useful for high-volume applications where you want to reduce costs or data volume while still maintaining visibility into your LLM usage. A sampling rate of 1.0 sends all traces, while 0.5 would send approximately 50% of traces.

##### 

Sampling is deterministic: when you provide a `session_id`, all traces within that session will be consistently included or excluded together. This ensures you always see complete sessions in your observability platform rather than fragmented data.

You’ll see full sessions per destination, but not necessarily the same sessions across all destinations.

## Privacy Mode

Each destination can optionally enable **Privacy Mode** to exclude prompt and completion content from traces. When Privacy Mode is enabled, the following data is stripped before sending traces:

- **Input messages** (prompts sent to the model)
- **Output choices** (completions returned by the model)

All other trace data — including token counts, costs, timing, model information, and custom metadata — is still sent normally.

This is useful when you want to monitor LLM usage metrics and costs without exposing the actual content of conversations, for example to comply with data privacy regulations or internal policies.

To enable Privacy Mode, toggle the **Privacy Mode** checkbox in the **Privacy** section when configuring a destination.

##### 

Privacy Mode is configured per destination. You can send full traces to one destination for debugging while sending privacy-redacted traces to another for cost monitoring.

## Security

Your destination credentials are encrypted before being stored and are only decrypted when sending traces. Traces are sent asynchronously after requests complete, so enabling broadcast does not add latency to your API responses.

## Organization Support

Broadcast can be configured at both the individual user level and the organization level. Organization admins can set up shared destinations that apply to all API keys within the organization, ensuring consistent observability across your team.

## Walkthroughs

Step-by-step guides for configuring specific broadcast destinations:

- [Arize AI](../arize/index.md) - ML observability and monitoring
- [Braintrust](../braintrust/index.md) - LLM evaluation and monitoring
- [ClickHouse](../clickhouse/index.md) - Real-time analytics database
- [Comet Opik](../opik/index.md) - LLM evaluation and testing
- [Datadog](../datadog/index.md) - Full-stack monitoring and analytics
- [Grafana Cloud](../grafana/index.md) - Observability and monitoring platform
- [Langfuse](../langfuse/index.md) - Open-source LLM engineering platform
- [LangSmith](../langsmith/index.md) - LangChain observability and debugging
- [New Relic](../newrelic/index.md) - Full-stack observability platform
- [OpenTelemetry Collector](../otel-collector/index.md) - Send traces to any OTLP-compatible backend
- [PostHog](../posthog/index.md) - Product analytics with LLM tracking
- [S3 / S3-Compatible](../s3/index.md) - Store traces in S3, R2, or compatible storage
- [Sentry](../sentry/index.md) - Application monitoring and error tracking
- [Snowflake](../snowflake/index.md) - Cloud data warehouse for analytics
- [W&B Weave](../weave/index.md) - LLM observability and tracking
- [Webhook](../webhook/index.md) - Send traces to any HTTP endpoint
