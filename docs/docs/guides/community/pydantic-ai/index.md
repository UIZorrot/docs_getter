---
source_url: "https://openrouter.ai/docs/guides/community/pydantic-ai"
title: "PydanticAI Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:55.437224+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# PydanticAI

Using OpenRouter with PydanticAI

## Using PydanticAI

[PydanticAI](https://github.com/pydantic/pydantic-ai) provides a high-level interface for working with various LLM providers, including OpenRouter.

### Installation

```
|  |  |
| --- | --- |
| $ | pip install 'pydantic-ai-slim[openai]' |
```

### Configuration

You can use OpenRouter with PydanticAI through its OpenAI-compatible interface:

```
|  |  |
| --- | --- |
| 1 | from pydantic_ai import Agent |
| 2 | from pydantic_ai.models.openai import OpenAIModel |
| 3 |  |
| 4 | model = OpenAIModel( |
| 5 | "anthropic/claude-3.5-sonnet",  # or any other OpenRouter model |
| 6 | base_url="https://openrouter.ai/api/v1", |
| 7 | api_key="sk-or-...", |
| 8 | ) |
| 9 |  |
| 10 | agent = Agent(model) |
| 11 | result = await agent.run("What is the meaning of life?") |
| 12 | print(result) |
```

For more details about using PydanticAI with OpenRouter, see the [PydanticAI documentation](https://ai.pydantic.dev/models).
