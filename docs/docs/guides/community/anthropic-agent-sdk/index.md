---
source_url: "https://openrouter.ai/docs/guides/community/anthropic-agent-sdk"
title: "Anthropic Agent SDK Integration | OpenRouter SDK Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:33.714557+00:00"
---
[Community](../frameworks-and-integrations-overview/index.md)

# Anthropic Agent SDK

Using OpenRouter with the Anthropic Agent SDK

The [Anthropic Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) lets you build AI agents programmatically using Python or TypeScript. Since the Agent SDK uses Claude Code as its runtime, you can connect it to OpenRouter using the same environment variables.

## Configuration

Set the following environment variables before running your agent:

```
|  |  |
| --- | --- |
| $ | export ANTHROPIC_BASE_URL="https://openrouter.ai/api" |
| $ | export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY" |
| $ | export ANTHROPIC_API_KEY="" # Important: Must be explicitly empty |
```

## TypeScript Example

Install the SDK:

```
|  |  |
| --- | --- |
| $ | npm install @anthropic-ai/claude-agent-sdk |
```

Create an agent that uses OpenRouter:

```
|  |  |
| --- | --- |
| 1 | import { query } from "@anthropic-ai/claude-agent-sdk"; |
| 2 |  |
| 3 | // Environment variables should be set before running: |
| 4 | // ANTHROPIC_BASE_URL=https://openrouter.ai/api |
| 5 | // ANTHROPIC_AUTH_TOKEN=your_openrouter_api_key |
| 6 | // ANTHROPIC_API_KEY="" |
| 7 |  |
| 8 | async function main() { |
| 9 | for await (const message of query({ |
| 10 | prompt: "Find and fix the bug in auth.py", |
| 11 | options: { |
| 12 | allowedTools: ["Read", "Edit", "Bash"], |
| 13 | }, |
| 14 | })) { |
| 15 | if (message.type === "assistant") { |
| 16 | console.log(message.message.content); |
| 17 | } |
| 18 | } |
| 19 | } |
| 20 |  |
| 21 | main(); |
```

## Python Example

Install the SDK:

```
|  |  |
| --- | --- |
| $ | pip install claude-agent-sdk |
```

Create an agent that uses OpenRouter:

```
|  |  |
| --- | --- |
| 1 | import asyncio |
| 2 | from claude_agent_sdk import query, ClaudeAgentOptions |
| 3 |  |
| 4 | # Environment variables should be set before running: |
| 5 | # ANTHROPIC_BASE_URL=https://openrouter.ai/api |
| 6 | # ANTHROPIC_AUTH_TOKEN=your_openrouter_api_key |
| 7 | # ANTHROPIC_API_KEY="" |
| 8 |  |
| 9 | async def main(): |
| 10 | async for message in query( |
| 11 | prompt="Find and fix the bug in auth.py", |
| 12 | options=ClaudeAgentOptions( |
| 13 | allowed_tools=["Read", "Edit", "Bash"] |
| 14 | ) |
| 15 | ): |
| 16 | print(message) |
| 17 |  |
| 18 | asyncio.run(main()) |
```

##### 

**Tip:** The Agent SDK inherits all the same model override capabilities as Claude Code. You can use `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`, and other environment variables to route your agent to different models on OpenRouter. See the [Claude Code integration guide](../../coding-agents/claude-code-integration/index.md) for more details.
