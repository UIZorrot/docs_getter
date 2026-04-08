---
source_url: "https://openrouter.ai/docs/guides/community/arize"
title: "Arize Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:34.293299+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# Arize

Using OpenRouter with Arize

## Using Arize

[Arize](https://arize.com/) provides observability and tracing for LLM applications. Since OpenRouter uses the OpenAI API schema, you can utilize Arize’s OpenInference auto-instrumentation with the OpenAI SDK to automatically trace and monitor your OpenRouter API calls.

### Installation

```
|  |  |
| --- | --- |
| $ | pip install openinference-instrumentation-openai openai arize-otel |
```

### Prerequisites

- OpenRouter account and API key
- Arize account with Space ID and API Key

### Why OpenRouter Works with Arize

Arize’s OpenInference auto-instrumentation works with OpenRouter because:

1. **OpenRouter provides a fully OpenAI-API-compatible endpoint** - The `/v1` endpoint mirrors OpenAI’s schema
2. **Reuse official OpenAI SDKs** - Point the OpenAI client’s `base_url` to OpenRouter
3. **Automatic instrumentation** - OpenInference hooks into OpenAI SDK calls seamlessly

### Configuration

Set up your environment variables:

Environment Setup

```
|  |  |
| --- | --- |
| 1 | import os |
| 2 |  |
| 3 | # Set your OpenRouter API key |
| 4 | os.environ["OPENAI_API_KEY"] = "${API_KEY_REF}" |
```

### Simple LLM Call

Initialize Arize and instrument your OpenAI client to automatically trace OpenRouter calls:

Basic Integration

```
|  |  |
| --- | --- |
| 1 | from arize.otel import register |
| 2 | from openinference.instrumentation.openai import OpenAIInstrumentor |
| 3 | import openai |
| 4 |  |
| 5 | # Initialize Arize and register the tracer provider |
| 6 | tracer_provider = register( |
| 7 | space_id="your-space-id", |
| 8 | api_key="your-arize-api-key", |
| 9 | project_name="your-project-name", |
| 10 | ) |
| 11 |  |
| 12 | # Instrument OpenAI SDK |
| 13 | OpenAIInstrumentor().instrument(tracer_provider=tracer_provider) |
| 14 |  |
| 15 | # Configure OpenAI client for OpenRouter |
| 16 | client = openai.OpenAI( |
| 17 | base_url="https://openrouter.ai/api/v1", |
| 18 | api_key="your_openrouter_api_key", |
| 19 | default_headers={ |
| 20 | "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional: Your site URL |
| 21 | "X-OpenRouter-Title": "<YOUR_SITE_NAME>",      # Optional: Your site name |
| 22 | } |
| 23 | ) |
| 24 |  |
| 25 | # Make a traced chat completion request |
| 26 | response = client.chat.completions.create( |
| 27 | model="meta-llama/llama-3.1-8b-instruct:free", |
| 28 | messages=[ |
| 29 | {"role": "user", "content": "Write a haiku about observability."} |
| 30 | ], |
| 31 | ) |
| 32 |  |
| 33 | # Print the assistant's reply |
| 34 | print(response.choices[0].message.content) |
```

### What Gets Traced

All OpenRouter model calls are automatically traced and include:

- Request/response data and timing
- Model name and provider information
- Token usage and cost data (when supported)
- Error handling and debugging information

### JavaScript/TypeScript Support

OpenInference also provides instrumentation for the OpenAI JavaScript/TypeScript SDK, which works with OpenRouter. For setup and examples, please refer to the [OpenInference JavaScript examples for OpenAI](https://github.com/Arize-ai/openinference/tree/main/js).

### Common Issues

- **API Key**: Use your OpenRouter API key, not OpenAI’s
- **Model Names**: Use exact model names from [OpenRouter’s model list](https://openrouter.ai/models)
- **Rate Limits**: Check your OpenRouter dashboard for usage limits

### Learn More

- **Arize OpenRouter Integration**: [https://arize.com/docs/ax/integrations/llm-providers/openrouter/openrouter-tracing](https://arize.com/docs/ax/integrations/llm-providers/openrouter/openrouter-tracing)
- **OpenRouter Quick Start Guide**: [https://openrouter.ai/docs/quickstart](../../../quickstart/index.md)
- **OpenInference OpenAI Instrumentation**: [https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-openai](https://github.com/Arize-ai/openinference/tree/main/python/instrumentation/openinference-instrumentation-openai)
