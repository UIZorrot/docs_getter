---
source_url: "https://openrouter.ai/docs/guides/community/langfuse"
title: "Langfuse Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:55.564495+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# Langfuse

Using OpenRouter with Langfuse

##### 

Looking to auto-instrument without client code? Check out [OpenRouter Broadcast](../../features/broadcast/langfuse/index.md) to automatically send traces to Langfuse.

## Using Langfuse

[Langfuse](https://langfuse.com/) provides observability and analytics for LLM applications. Since OpenRouter uses the OpenAI API schema, you can utilize Langfuse’s native integration with the OpenAI SDK to automatically trace and monitor your OpenRouter API calls.

### Installation

```
|  |  |
| --- | --- |
| $ | pip install langfuse openai |
```

### Configuration

Set up your environment variables:

Environment Setup

```
|  |  |
| --- | --- |
| 1 | import os |
| 2 |  |
| 3 | # Set your Langfuse API keys |
| 4 | LANGFUSE_SECRET_KEY="sk-lf-..." |
| 5 | LANGFUSE_PUBLIC_KEY="pk-lf-..." |
| 6 | # EU region |
| 7 | LANGFUSE_HOST="https://cloud.langfuse.com" |
| 8 | # US region |
| 9 | # LANGFUSE_HOST="https://us.cloud.langfuse.com" |
| 10 |  |
| 11 | # Set your OpenRouter API key |
| 12 | os.environ["OPENAI_API_KEY"] = "${API_KEY_REF}" |
```

### Simple LLM Call

Since OpenRouter provides an OpenAI-compatible API, you can use the Langfuse OpenAI SDK wrapper to automatically log OpenRouter calls as generations in Langfuse:

Basic Integration

```
|  |  |
| --- | --- |
| 1 | # Import the Langfuse OpenAI SDK wrapper |
| 2 | from langfuse.openai import openai |
| 3 |  |
| 4 | # Create an OpenAI client with OpenRouter's base URL |
| 5 | client = openai.OpenAI( |
| 6 | base_url="https://openrouter.ai/api/v1", |
| 7 | default_headers={ |
| 8 | "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional: Your site URL |
| 9 | "X-OpenRouter-Title": "<YOUR_SITE_NAME>",      # Optional: Your site name |
| 10 | } |
| 11 | ) |
| 12 |  |
| 13 | # Make a chat completion request |
| 14 | response = client.chat.completions.create( |
| 15 | model="anthropic/claude-3.5-sonnet", |
| 16 | messages=[ |
| 17 | {"role": "system", "content": "You are a helpful assistant."}, |
| 18 | {"role": "user", "content": "Tell me a fun fact about space."} |
| 19 | ], |
| 20 | name="fun-fact-request"  # Optional: Name of the generation in Langfuse |
| 21 | ) |
| 22 |  |
| 23 | # Print the assistant's reply |
| 24 | print(response.choices[0].message.content) |
```

### Advanced Tracing with Nested Calls

Use the `@observe()` decorator to capture execution details of functions with nested LLM calls:

Nested Function Tracing

```
|  |  |
| --- | --- |
| 1 | from langfuse import observe |
| 2 | from langfuse.openai import openai |
| 3 |  |
| 4 | # Create an OpenAI client with OpenRouter's base URL |
| 5 | client = openai.OpenAI( |
| 6 | base_url="https://openrouter.ai/api/v1", |
| 7 | ) |
| 8 |  |
| 9 | @observe()  # This decorator enables tracing of the function |
| 10 | def analyze_text(text: str): |
| 11 | # First LLM call: Summarize the text |
| 12 | summary_response = summarize_text(text) |
| 13 | summary = summary_response.choices[0].message.content |
| 14 |  |
| 15 | # Second LLM call: Analyze the sentiment of the summary |
| 16 | sentiment_response = analyze_sentiment(summary) |
| 17 | sentiment = sentiment_response.choices[0].message.content |
| 18 |  |
| 19 | return { |
| 20 | "summary": summary, |
| 21 | "sentiment": sentiment |
| 22 | } |
| 23 |  |
| 24 | @observe()  # Nested function to be traced |
| 25 | def summarize_text(text: str): |
| 26 | return client.chat.completions.create( |
| 27 | model="openai/gpt-3.5-turbo", |
| 28 | messages=[ |
| 29 | {"role": "system", "content": "You summarize texts in a concise manner."}, |
| 30 | {"role": "user", "content": f"Summarize the following text:\n{text}"} |
| 31 | ], |
| 32 | name="summarize-text" |
| 33 | ) |
| 34 |  |
| 35 | @observe()  # Nested function to be traced |
| 36 | def analyze_sentiment(summary: str): |
| 37 | return client.chat.completions.create( |
| 38 | model="openai/gpt-3.5-turbo", |
| 39 | messages=[ |
| 40 | {"role": "system", "content": "You analyze the sentiment of texts."}, |
| 41 | {"role": "user", "content": f"Analyze the sentiment of the following summary:\n{summary}"} |
| 42 | ], |
| 43 | name="analyze-sentiment" |
| 44 | ) |
| 45 |  |
| 46 | # Example usage |
| 47 | text_to_analyze = "OpenRouter's unified API has significantly advanced the field of AI development, setting new standards for model accessibility." |
| 48 | result = analyze_text(text_to_analyze) |
| 49 | print(result) |
```

### Learn More

- **Langfuse OpenRouter Integration**: [https://langfuse.com/docs/integrations/other/openrouter](https://langfuse.com/docs/integrations/other/openrouter)
- **OpenRouter Quick Start Guide**: [https://openrouter.ai/docs/quickstart](../../../quickstart/index.md)
- **Langfuse `@observe()` Decorator**: [https://langfuse.com/docs/sdk/python/decorators](https://langfuse.com/docs/sdk/python/decorators)
