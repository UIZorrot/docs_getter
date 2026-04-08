---
source_url: "https://openrouter.ai/docs/sdks/agentic-usage"
title: "Agentic Usage | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:43.970922+00:00"
---
# Agentic Usage

Add OpenRouter SDK skills to your AI coding assistant

Give your AI coding assistant the knowledge to work with the OpenRouter SDK
by installing our official skill. This enables AI agents to understand the
SDK’s APIs, patterns, and best practices when helping you write code.

## Quick Start

Run this command in your project directory:

```
|  |  |
| --- | --- |
| $ | npx add-skill OpenRouterTeam/agent-skills |
```

This installs the OpenRouter SDK skill, which teaches your AI assistant how
to use the SDK effectively.

## Supported AI Coding Assistants

The skill works with any AI coding assistant that supports the skills format:

| Assistant | Status |
| --- | --- |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Supported |
| [OpenCode](https://opencode.ai/) | Supported |
| [Cursor](https://cursor.com/) | Supported |
| [GitHub Copilot](https://github.com/features/copilot) | Supported |
| [Codex](https://openai.com/index/openai-codex) | Supported |
| [Amp](https://amp.dev/) | Supported |
| [Roo Code](https://roo.dev/) | Supported |
| [Antigravity](https://antigravity.dev/) | Supported |

## What the Skill Provides

Once installed, your AI coding assistant will have knowledge of:

- **SDK Installation & Setup** - How to install and configure the OpenRouter
  SDK in TypeScript projects
- **callModel API** - The recommended approach for making AI model calls with
  full type safety and streaming support
- **Chat Completions** - Working with the chat API for conversations
- **Embeddings** - Generating embeddings for semantic search and RAG
- **Error Handling** - Proper error handling patterns and Result types
- **Streaming** - Real-time streaming responses
- **Tool Use** - Implementing function calling and tools

## Example Usage

After installing the skill, your AI assistant can help you with tasks like:

**“Help me set up OpenRouter in my project”**

The assistant will know to use:

```
|  |  |
| --- | --- |
| 1 | import { callModel } from '@openrouter/agent'; |
| 2 |  |
| 3 | const response = await callModel({ |
| 4 | model: 'anthropic/claude-sonnet-4', |
| 5 | messages: [ |
| 6 | { role: 'user', content: 'Hello!' } |
| 7 | ] |
| 8 | }); |
```

**“Add streaming to my OpenRouter call”**

The assistant understands the streaming API:

```
|  |  |
| --- | --- |
| 1 | import { callModel } from '@openrouter/agent'; |
| 2 |  |
| 3 | const stream = await callModel({ |
| 4 | model: 'anthropic/claude-sonnet-4', |
| 5 | messages: [{ role: 'user', content: 'Tell me a story' }], |
| 6 | stream: true |
| 7 | }); |
| 8 |  |
| 9 | for await (const chunk of stream) { |
| 10 | process.stdout.write(chunk.choices[0]?.delta?.content ?? ''); |
| 11 | } |
```

## Updating the Skill

To get the latest SDK documentation, re-run the install command:

```
|  |  |
| --- | --- |
| $ | npx add-skill OpenRouterTeam/agent-skills |
```

The skill is automatically updated when new SDK versions are released.

## Manual Installation

If you prefer to install manually, add the skill file to your project’s
`.skills/` directory:

```
|  |  |
| --- | --- |
| $ | mkdir -p .skills |
| $ | curl -o .skills/openrouter-sdk.md \ |
| > | https://raw.githubusercontent.com/OpenRouterTeam/agent-skills/main/skills/typescript-sdk/SKILL.md |
```

## Repository

The skill source is available at:
[github.com/OpenRouterTeam/agent-skills](https://github.com/OpenRouterTeam/agent-skills)

Contributions and feedback are welcome.
