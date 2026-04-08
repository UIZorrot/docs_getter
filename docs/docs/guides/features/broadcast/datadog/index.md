---
source_url: "https://openrouter.ai/docs/guides/features/broadcast/datadog"
title: "Datadog Broadcast | OpenRouter Observability | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:36.269433+00:00"
---
[Features](../../presets/index.md)[Broadcast](../overview/index.md)

# Datadog

Send traces to Datadog

With [Datadog LLM Observability](https://docs.datadoghq.com/llm_observability), you can investigate the root cause of issues, monitor operational performance, and evaluate the quality, privacy, and safety of your LLM applications.

## Step 1: Create a Datadog API key

In Datadog, go to **Organization Settings > API Keys** and create a new key.

## Step 2: Enable Broadcast in OpenRouter

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

## Step 3: Configure Datadog

Click the edit icon next to **Datadog** and enter:

- **Api Key**: Your Datadog API key
- **Ml App**: A name for your application (e.g., “production-app”)
- **Url** (optional): Default is `https://api.us5.datadoghq.com`. Change for other regions

![Datadog Configuration](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/bd0388077ffa2902197f1d1fa6119f5ce77bf529fe0d8c7c4c95f9fb46059daf/content/pages/features/broadcast/broadcast-datadog-config.png)

## Step 4: Test and save

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

![Datadog Configured](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/755c64c80cd8210cb44151d7d67c6937a16c70eb7cc3abe752c788bf72b5dc20/content/pages/features/broadcast/broadcast-datadog-configured.png)

## Step 5: Send a test trace

Make an API request through OpenRouter and view the trace in Datadog.

![Datadog Trace](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/2bf9b44fd78abdb48c8a14645b5113b0f0ce1b754828a17fc07d1fe7cdcbe1e0/content/pages/features/broadcast/broadcast-datadog-trace.png)

## Custom Metadata

Datadog LLM Observability supports tags and custom metadata for organizing and filtering your traces.

### Supported Metadata Keys

| Key | Datadog Mapping | Description |
| --- | --- | --- |
| `trace_id` | Trace ID | Group multiple requests into a single trace |
| `trace_name` | Span Name | Custom name for the root span |
| `span_name` | Span Name | Name for intermediate workflow spans |
| `generation_name` | Span Name | Name for the LLM span |

### Tags and Metadata

Datadog uses tags for filtering and grouping traces. The following are automatically added as tags:

- `service:{ml_app}` - Your configured ML App name
- `user_id:{user}` - From the `user` field in your request

Any additional keys in `trace` are passed to the span’s `meta` object and can be viewed in Datadog’s trace details.

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Hello!" }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_name": "Customer Support Bot", |
| 8 | "environment": "production", |
| 9 | "team": "support", |
| 10 | "ticket_id": "TICKET-1234" |
| 11 | } |
| 12 | } |
```

### Viewing in Datadog

In Datadog LLM Observability, you can:

- Filter traces by tags in the trace list
- View custom metadata in the trace details panel
- Create monitors and dashboards using metadata fields

## Privacy Mode

When [Privacy Mode](../index.md) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](../index.md) for details.
