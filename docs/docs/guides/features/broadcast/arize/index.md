---
source_url: "https://openrouter.ai/docs/guides/features/broadcast/arize"
title: "Broadcast to Arize AI | OpenRouter Observability | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:35.944874+00:00"
---
[Features](../../presets/index.md)[Broadcast](../overview/index.md)

# Arize AI

Send traces to Arize AI

[Arize AX](https://arize.com/) is an evaluation and observability platform developed by Arize AI; it offers tools for agent tracing, evals, prompt optimization, and more.

## Step 1: Get your Arize credentials

In Arize, navigate to your space settings to find your API key and space key:

1. Log in to your Arize account
2. Go to **Space Settings** to find your Space Key
3. Go to **API Keys** to create or copy your API key
4. Note the Model ID you want to use for organizing traces

## Step 2: Enable Broadcast in OpenRouter

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

## Step 3: Configure Arize AI

Click the edit icon next to **Arize AI** and enter:

- **Api Key**: Your Arize API key
- **Space Key**: Your Arize space key
- **Model Id**: The model identifier for organizing your traces in Arize
- **Base Url** (optional): Default is `https://otlp.arize.com`

## Step 4: Test and save

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

## Step 5: Send a test trace

Make an API request through OpenRouter and view the trace in your Arize
dashboard under the specified model.

![Arize Trace View](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/a917bd16b2036c129bd72451d4650953812a85f8c7585dd39804fceef83857d9/content/pages/features/broadcast/broadcast-arize-trace.png)

## Custom Metadata

Arize uses the [OpenInference](https://github.com/Arize-ai/openinference) semantic convention for tracing. Custom metadata from the `trace` field is sent as span attributes in the OTLP payload.

### Supported Metadata Keys

| Key | Arize Mapping | Description |
| --- | --- | --- |
| `trace_id` | Trace ID | Group multiple requests into a single trace |
| `trace_name` | Span Name | Custom name for the root trace |
| `span_name` | Span Name | Name for intermediate spans in the hierarchy |
| `generation_name` | Span Name | Name for the LLM generation span |
| `parent_span_id` | Parent Span ID | Link to an existing span in your trace hierarchy |

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Classify this text..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_id": "classification_pipeline_001", |
| 8 | "trace_name": "Text Classification", |
| 9 | "generation_name": "Classify Sentiment", |
| 10 | "dataset": "customer_feedback", |
| 11 | "experiment_id": "exp_v3" |
| 12 | } |
| 13 | } |
```

### Additional Context

- Custom metadata keys from `trace` are included as span attributes under the `metadata.*` namespace
- The `user` field maps to user identification in span attributes
- The `session_id` field maps to session tracking in span attributes
- Token usage, costs, and model parameters are automatically included as OpenInference-compatible attributes

## Privacy Mode

When [Privacy Mode](../index.md) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](../index.md) for details.
