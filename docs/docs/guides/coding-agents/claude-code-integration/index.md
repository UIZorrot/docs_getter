---
source_url: "https://openrouter.ai/docs/guides/coding-agents/claude-code-integration"
title: "Integration with Claude Code | OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:33.096940+00:00"
---
[Guides](../../administration/activity-export/index.md)[Coding Agents](../automatic-code-review/index.md)

# Claude Code

Use Claude Code with OpenRouter

##### 

Claude Code with OpenRouter is only guaranteed to work with the Anthropic first-party provider. For maximum compatibility, we recommend setting [Anthropic 1P as top priority provider](../../../features/provider-routing/index.md) when using Claude Code.

## Why Use OpenRouter with Claude Code?

OpenRouter adds a reliability and management layer between Claude Code and Anthropic’s API, giving you and your organization several key benefits.

### Provider Failover for High Availability

Anthropic’s API occasionally experiences outages or rate limiting. When you route Claude Code through OpenRouter, your requests automatically fail over between multiple Anthropic providers. If one provider is unavailable or rate-limited, OpenRouter seamlessly routes to another, keeping your coding sessions uninterrupted.

### Organizational Budget Controls

For teams and organizations, OpenRouter provides centralized budget management. You can set spending limits, allocate credits across team members, and prevent unexpected cost overruns. This is especially valuable when multiple developers are using Claude Code across your organization.

### Usage Visibility and Analytics

OpenRouter gives you complete visibility into how Claude Code is being used across your team. Track usage patterns, monitor costs in real-time, and understand which projects or team members are consuming the most resources. All of this data is available in your [OpenRouter Activity Dashboard](https://openrouter.ai/activity).

## Quick Start

This guide will get you running [Claude Code](https://code.claude.com/docs/en/overview) powered by OpenRouter in just a few minutes.

### Step 1: Install Claude Code

###### Native Install (Recommended)

###### npm

**macOS, Linux, WSL:**

```
|  |  |
| --- | --- |
| $ | curl -fsSL https://claude.ai/install.sh | bash |
```

**Windows PowerShell:**

```
|  |  |
| --- | --- |
| 1 | irm https://claude.ai/install.ps1 | iex |
```

### Step 2: Connect Claude to OpenRouter

Instead of logging in with Anthropic directly, connect Claude Code to OpenRouter.
This requires setting a few environment variables.

Requirements:

1. Use `https://openrouter.ai/api` for the base url
2. Provide your [OpenRouter API key](https://openrouter.ai/settings/keys) as the auth token
3. **Important:** Explicitly blank out the Anthropic API key to prevent conflicts

###### Shell Profile

###### Project Settings File

Add these environment variables to your shell profile:

```
|  |  |
| --- | --- |
| $ | # Open your shell profile in nano |
| $ | nano ~/.zshrc  # or ~/.bashrc for Bash users |
| $ |  |
| $ | # Add these lines to the file: |
| $ | export OPENROUTER_API_KEY="<your-openrouter-api-key>" |
| $ | export ANTHROPIC_BASE_URL="https://openrouter.ai/api" |
| $ | export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY" |
| $ | export ANTHROPIC_API_KEY="" # Important: Must be explicitly empty |
| $ |  |
| $ | # After saving, restart your terminal for changes to take effect |
```

##### 

**Persistence:** We recommend adding these lines to your shell profile (`~/.bashrc`, `~/.zshrc`, or `~/.config/fish/config.fish`).

##### 

**Variable Location:** Do not put these in a project-level `.env` file. The native Claude Code installer does not read standard `.env` files.

**Previous Login:** If you were previously logged in to Claude Code with Anthropic, run `/logout` in a Claude Code session to clear cached credentials before the OpenRouter configuration takes effect.

### Step 3: Start your session

Navigate to your project directory and start Claude Code:

```
|  |  |
| --- | --- |
| $ | cd /path/to/your/project |
| $ | claude |
```

You are now connected! Any prompt you send will be routed through OpenRouter.

### Step 4: Verify

You can confirm your connection by running the `/status` command inside Claude Code.

```
|  |
| --- |
| > /status |
| Auth token: ANTHROPIC_AUTH_TOKEN |
| Anthropic base URL: https://openrouter.ai/api |
```

You can also check the [OpenRouter Activity Dashboard](https://openrouter.ai/activity) to see your requests appearing in real-time.

## How It Works

OpenRouter exposes an input that is compatible with the Anthropic Messages API.

1. **Direct Connection:** When you set `ANTHROPIC_BASE_URL` to `https://openrouter.ai/api`, Claude Code speaks its native protocol directly to OpenRouter. No local proxy server is required.
2. **Anthropic Skin:** OpenRouter’s “Anthropic Skin” behaves exactly like the Anthropic API. It handles model mapping and passes through advanced features like “Thinking” blocks and native tool use.
3. **Billing:** You are billed using your OpenRouter credits. Usage (including reasoning tokens) appears in your OpenRouter dashboard.

## Configuring Models

Claude Code uses several environment variables to determine which models to use for different tasks. You can override these to route each role through a specific model:

```
|  |  |
| --- | --- |
| $ | export ANTHROPIC_DEFAULT_OPUS_MODEL="anthropic/claude-opus-4.6" |
| $ | export ANTHROPIC_DEFAULT_SONNET_MODEL="anthropic/claude-sonnet-4.6" |
| $ | export ANTHROPIC_DEFAULT_HAIKU_MODEL="anthropic/claude-haiku-4.5" |
| $ | export CLAUDE_CODE_SUBAGENT_MODEL="anthropic/claude-opus-4.6" |
```

| Variable | Description |
| --- | --- |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | The model used for Opus-class tasks (e.g. complex reasoning) |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | The model used for Sonnet-class tasks (e.g. general coding) |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | The model used for Haiku-class tasks (e.g. quick completions) |
| `CLAUDE_CODE_SUBAGENT_MODEL` | The model used for sub-agent tasks spawned by Claude Code |

Add these to the same shell profile or project settings file where you set `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN`.

Claude Code is optimized for Anthropic models and may not work correctly with other providers.

## Agent SDK

The [Anthropic Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview) lets you build AI agents programmatically using Python or TypeScript. Since the Agent SDK uses Claude Code as its runtime, you can connect it to OpenRouter using the same environment variables described above.

For complete setup instructions and code examples, see our [Anthropic Agent SDK integration guide](../../community/anthropic-agent-sdk/index.md).

## GitHub Action

You can use OpenRouter with the official [Claude Code GitHub Action](https://github.com/anthropics/claude-code-action).To adapt the [example workflow](https://github.com/anthropics/claude-code-action/blob/main/examples/claude.yml) for OpenRouter, make two changes to the action step:

1. Pass your OpenRouter API key via `anthropic_api_key` (store it as a GitHub secret named `OPENROUTER_API_KEY`)
2. Set the `ANTHROPIC_BASE_URL` environment variable to `https://openrouter.ai/api`

```
|  |  |
| --- | --- |
| 1 | - name: Run Claude Code |
| 2 | uses: anthropics/claude-code-action@v1 |
| 3 | with: |
| 4 | anthropic_api_key: ${{ secrets.OPENROUTER_API_KEY }} |
| 5 | env: |
| 6 | ANTHROPIC_BASE_URL: https://openrouter.ai/api |
```

## Cost Tracking Statusline

You can add a custom statusline to Claude Code that tracks your OpenRouter API costs in real-time. The statusline displays the provider, model, cumulative cost, and cache discounts for your session.

![Claude Code statusline showing OpenRouter cost tracking](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5bc3af530c4a0111317cbdcee893be444718c676f3f80bf0860141cffcb5ee1b/content/pages/guides/claude-code-statusline.png)

Download the statusline scripts from the [openrouter-examples repository](https://github.com/OpenRouterTeam/openrouter-examples/tree/main/claude-code), make them executable, and add the following to your `~/.claude/settings.json`:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "statusLine": { |
| 3 | "type": "command", |
| 4 | "command": "/path/to/statusline.sh" |
| 5 | } |
| 6 | } |
```

The script uses your `ANTHROPIC_AUTH_TOKEN` environment variable, which should already be set to your OpenRouter API key if you followed the setup above.

## Troubleshooting

- **Auth Errors:** Ensure `ANTHROPIC_API_KEY` is set to an empty string (`""`). If it is unset (null), Claude Code might fall back to its default behavior and try to authenticate with Anthropic servers.
- **Context Length Errors:** If you hit context limits, consider breaking your task into smaller chunks or starting a new session.
- **Privacy:** OpenRouter does not log your source code prompts unless you explicitly opt-in to prompt logging in your account settings. See our [Privacy Policy](https://openrouter.ai/privacy) for details.
