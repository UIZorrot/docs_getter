---
source_url: "https://openrouter.ai/docs/guides/community/langchain"
title: "LangChain Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:54.089473+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# LangChain

Using OpenRouter with LangChain

## Using LangChain

LangChain provides a standard interface for working with chat models. You can use OpenRouter with LangChain using the dedicated `ChatOpenRouter` integration packages. For more details on LangChain’s model interface, see the [LangChain Models documentation](https://docs.langchain.com/oss/python/langchain/models).

**Resources:**

- [LangChain Python integration](https://docs.langchain.com/oss/python/integrations/chat/openrouter): [langchain-openrouter on PyPI](https://pypi.org/project/langchain-openrouter)
- [LangChain JavaScript integration](https://docs.langchain.com/oss/javascript/integrations/chat/openrouter): [@langchain/openrouter on npm](https://www.npmjs.com/package/@langchain/openrouter)

```
|  |  |
| --- | --- |
| 1 | import { ChatOpenRouter } from "@langchain/openrouter"; |
| 2 |  |
| 3 | const model = new ChatOpenRouter( |
| 4 | "anthropic/claude-sonnet-4.6", |
| 5 | { temperature: 0.8 } |
| 6 | ); |
| 7 |  |
| 8 | // Example usage |
| 9 | const response = await model.invoke([ |
| 10 | { role: "system", content: "You are a helpful assistant." }, |
| 11 | { role: "user", content: "Hello, how are you?" }, |
| 12 | ]); |
```

For full documentation — including streaming, tool calling, structured output, reasoning, multimodal inputs, provider routing, and more — see the LangChain integration guides:

- [Python: ChatOpenRouter](https://docs.langchain.com/oss/python/integrations/chat/openrouter)
- [JavaScript: ChatOpenRouter](https://docs.langchain.com/oss/javascript/integrations/chat/openrouter)
