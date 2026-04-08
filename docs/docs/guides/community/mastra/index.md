---
source_url: "https://openrouter.ai/docs/guides/community/mastra"
title: "Mastra Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:55.197137+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# Mastra

Using OpenRouter with Mastra

## Mastra

Integrate OpenRouter with Mastra to access a variety of AI models through a unified interface. This guide provides complete examples from basic setup to advanced configurations.

### Step 1: Initialize a new Mastra project

The simplest way to start is using the automatic project creation:

```
|  |  |
| --- | --- |
| $ | # Create a new project using create-mastra |
| $ | npx create-mastra@latest |
```

You’ll be guided through prompts to set up your project. For this example, select:

- Name your project: my-mastra-openrouter-app
- Components: Agents (recommended)
- For default provider, select OpenAI (recommended) - we’ll configure OpenRouter manually later
- Optionally include example code

For detailed instructions on setting up a Mastra project manually or adding Mastra to an existing project, refer to the [official Mastra documentation](https://mastra.ai/en/docs/getting-started/installation).

### Step 2: Configure your environment variables

After creating your project with `create-mastra`, you’ll find a `.env.development` file in your project root. Since we selected OpenAI during setup but will be using OpenRouter instead:

1. Open the `.env.development` file
2. Remove or comment out the `OPENAI_API_KEY` line
3. Add your OpenRouter API key:

```
|  |
| --- |
| # .env.development |
| # OPENAI_API_KEY=your-openai-key  # Comment out or remove this line |
| OPENROUTER_API_KEY=sk-or-your-api-key-here |
```

You can also remove the `@ai-sdk/openai` package since we’ll be using OpenRouter instead:

```
|  |  |
| --- | --- |
| $ | npm uninstall @ai-sdk/openai |
```

```
|  |  |
| --- | --- |
| $ | npm install @openrouter/ai-sdk-provider |
```

### Step 3: Configure your agent to use OpenRouter

After setting up your Mastra project, you’ll need to modify the agent files to use OpenRouter instead of the default OpenAI provider.

If you used `create-mastra`, you’ll likely have a file at `src/mastra/agents/agent.ts` or similar. Replace its contents with:

```
|  |  |
| --- | --- |
| 1 | import { Agent } from '@mastra/core/agent'; |
| 2 | import { createOpenRouter } from '@openrouter/ai-sdk-provider'; |
| 3 |  |
| 4 | // Initialize OpenRouter provider |
| 5 | const openrouter = createOpenRouter({ |
| 6 | apiKey: process.env.OPENROUTER_API_KEY, |
| 7 | }); |
| 8 |  |
| 9 | // Create an agent |
| 10 | export const assistant = new Agent({ |
| 11 | model: openrouter('anthropic/claude-3-opus'), |
| 12 | name: 'Assistant', |
| 13 | instructions: |
| 14 | 'You are a helpful assistant with expertise in technology and science.', |
| 15 | }); |
```

Also make sure to update your Mastra entry point at `src/mastra/index.ts` to use your renamed agent:

```
|  |  |
| --- | --- |
| 1 | import { Mastra } from '@mastra/core'; |
| 2 |  |
| 3 | import { assistant } from './agents/agent'; // Update the import path if you used a different filename |
| 4 |  |
| 5 | export const mastra = new Mastra({ |
| 6 | agents: { assistant }, // Use the same name here as you exported from your agent file |
| 7 | }); |
```

### Step 4: Running the Application

Once you’ve configured your agent to use OpenRouter, you can run the Mastra development server:

```
|  |  |
| --- | --- |
| $ | npm run dev |
```

This will start the Mastra development server and make your agent available at:

- REST API endpoint: `http://localhost:4111/api/agents/assistant/generate`
- Interactive playground: `http://localhost:4111`

The Mastra playground provides a user-friendly interface where you can interact with your agent and test its capabilities without writing any additional code.

You can also test the API endpoint using curl if needed:

```
|  |  |
| --- | --- |
| $ | curl -X POST http://localhost:4111/api/agents/assistant/generate \ |
| > | -H "Content-Type: application/json" \ |
| > | -d '{"messages": ["What are the latest advancements in quantum computing?"]}' |
```

### Basic Integration with Mastra

The simplest way to integrate OpenRouter with Mastra is by using the OpenRouter AI provider with Mastra’s Agent system:

```
|  |  |
| --- | --- |
| 1 | import { Agent } from '@mastra/core/agent'; |
| 2 | import { createOpenRouter } from '@openrouter/ai-sdk-provider'; |
| 3 |  |
| 4 | // Initialize the OpenRouter provider |
| 5 | const openrouter = createOpenRouter({ |
| 6 | apiKey: process.env.OPENROUTER_API_KEY, |
| 7 | }); |
| 8 |  |
| 9 | // Create an agent using OpenRouter |
| 10 | const assistant = new Agent({ |
| 11 | model: openrouter('anthropic/claude-3-opus'), |
| 12 | name: 'Assistant', |
| 13 | instructions: 'You are a helpful assistant.', |
| 14 | }); |
| 15 |  |
| 16 | // Generate a response |
| 17 | const response = await assistant.generate([ |
| 18 | { |
| 19 | role: 'user', |
| 20 | content: 'Tell me about renewable energy sources.', |
| 21 | }, |
| 22 | ]); |
| 23 |  |
| 24 | console.log(response.text); |
```

### Advanced Configuration

For more control over your OpenRouter requests, you can pass additional configuration options:

```
|  |  |
| --- | --- |
| 1 | import { Agent } from '@mastra/core/agent'; |
| 2 | import { createOpenRouter } from '@openrouter/ai-sdk-provider'; |
| 3 |  |
| 4 | // Initialize with advanced options |
| 5 | const openrouter = createOpenRouter({ |
| 6 | apiKey: process.env.OPENROUTER_API_KEY, |
| 7 | extraBody: { |
| 8 | reasoning: { |
| 9 | max_tokens: 10, |
| 10 | }, |
| 11 | }, |
| 12 | }); |
| 13 |  |
| 14 | // Create an agent with model-specific options |
| 15 | const chefAgent = new Agent({ |
| 16 | model: openrouter('anthropic/claude-3.7-sonnet', { |
| 17 | extraBody: { |
| 18 | reasoning: { |
| 19 | max_tokens: 10, |
| 20 | }, |
| 21 | }, |
| 22 | }), |
| 23 | name: 'Chef', |
| 24 | instructions: 'You are a chef assistant specializing in French cuisine.', |
| 25 | }); |
```

### Provider-Specific Options

You can also pass provider-specific options in your requests:

```
|  |  |
| --- | --- |
| 1 | // Get a response with provider-specific options |
| 2 | const response = await chefAgent.generate([ |
| 3 | { |
| 4 | role: 'system', |
| 5 | content: |
| 6 | 'You are Chef Michel, a culinary expert specializing in ketogenic (keto) diet...', |
| 7 | providerOptions: { |
| 8 | // Provider-specific options - key can be 'anthropic' or 'openrouter' |
| 9 | anthropic: { |
| 10 | cacheControl: { type: 'ephemeral' }, |
| 11 | }, |
| 12 | }, |
| 13 | }, |
| 14 | { |
| 15 | role: 'user', |
| 16 | content: 'Can you suggest a keto breakfast?', |
| 17 | }, |
| 18 | ]); |
```

### Using Multiple Models with OpenRouter

OpenRouter gives you access to various models from different providers. Here’s how to use multiple models:

```
|  |  |
| --- | --- |
| 1 | import { Agent } from '@mastra/core/agent'; |
| 2 | import { createOpenRouter } from '@openrouter/ai-sdk-provider'; |
| 3 |  |
| 4 | const openrouter = createOpenRouter({ |
| 5 | apiKey: process.env.OPENROUTER_API_KEY, |
| 6 | }); |
| 7 |  |
| 8 | // Create agents using different models |
| 9 | const claudeAgent = new Agent({ |
| 10 | model: openrouter('anthropic/claude-3-opus'), |
| 11 | name: 'ClaudeAssistant', |
| 12 | instructions: 'You are a helpful assistant powered by Claude.', |
| 13 | }); |
| 14 |  |
| 15 | const gptAgent = new Agent({ |
| 16 | model: openrouter('openai/gpt-4'), |
| 17 | name: 'GPTAssistant', |
| 18 | instructions: 'You are a helpful assistant powered by GPT-4.', |
| 19 | }); |
| 20 |  |
| 21 | // Use different agents based on your needs |
| 22 | const claudeResponse = await claudeAgent.generate([ |
| 23 | { |
| 24 | role: 'user', |
| 25 | content: 'Explain quantum mechanics simply.', |
| 26 | }, |
| 27 | ]); |
| 28 | console.log(claudeResponse.text); |
| 29 |  |
| 30 | const gptResponse = await gptAgent.generate([ |
| 31 | { |
| 32 | role: 'user', |
| 33 | content: 'Explain quantum mechanics simply.', |
| 34 | }, |
| 35 | ]); |
| 36 | console.log(gptResponse.text); |
```

### Resources

For more information and detailed documentation, check out these resources:

- [OpenRouter Documentation](../../../index.md) - Learn about OpenRouter’s capabilities and available models
- [Mastra Documentation](https://mastra.ai/docs) - Comprehensive documentation for the Mastra framework
- [AI SDK Documentation](https://sdk.vercel.ai/docs) - Detailed information about the AI SDK that powers Mastra’s model interactions
