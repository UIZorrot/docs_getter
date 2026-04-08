---
source_url: "https://openrouter.ai/docs/guides/coding-agents/junie"
title: "Junie CLI Integration | OpenRouter JetBrains Junie Support | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:34.023578+00:00"
---
[Guides](../../administration/activity-export/index.md)[Coding Agents](../automatic-code-review/index.md)

# Junie CLI

Using OpenRouter with JetBrains Junie CLI

## Using Junie CLI with OpenRouter

[Junie CLI](https://junie.jetbrains.com/) is an agentic coding tool by JetBrains that provides an interactive terminal interface for developers to review, write, and modify code. By connecting Junie to OpenRouter, you can access hundreds of AI models from a single API key instead of managing separate keys for each provider.

### Why Use OpenRouter with Junie?

- **Access to hundreds of models** — Use models from Anthropic, OpenAI, Google, xAI, Meta, and many more through a single API key
- **Provider failover** — If one provider is unavailable or rate-limited, OpenRouter automatically routes to another
- **Centralized billing** — Track and manage spending across all models from your [OpenRouter dashboard](https://openrouter.ai/activity)
- **Team controls** — Set budgets and monitor usage across your organization

### Prerequisites

- [Junie CLI](https://junie.jetbrains.com/) installed (see [Step 1](#step-1-install-junie-cli) below)
- An [OpenRouter API key](https://openrouter.ai/settings/keys)

### Step 1: Install Junie CLI

###### Linux / macOS

###### Windows

###### Homebrew

```
|  |  |
| --- | --- |
| $ | curl -fsSL https://junie.jetbrains.com/install.sh | bash |
```

Verify the installation:

```
|  |  |
| --- | --- |
| $ | junie --version |
```

### Step 2: Configure OpenRouter

Junie supports OpenRouter as a built-in BYOK (Bring Your Own Key) provider. Set the `JUNIE_OPENROUTER_API_KEY` environment variable to connect Junie to OpenRouter:

###### Shell Profile (Recommended)

###### Inline

###### CI/CD

Add the environment variable to your shell profile for persistent configuration:

```
|  |  |
| --- | --- |
| $ | # Open your shell profile |
| $ | nano ~/.zshrc  # or ~/.bashrc for Bash users |
| $ |  |
| $ | # Add this line: |
| $ | export JUNIE_OPENROUTER_API_KEY="<your-openrouter-api-key>" |
```

After saving, restart your terminal or run `source ~/.zshrc` for changes to take effect.

##### 

Replace `<your-openrouter-api-key>` with your actual OpenRouter API key from the [API Keys page](https://openrouter.ai/settings/keys). Keys start with `sk-or-v1-`.

### Step 3: Start Coding

Navigate to your project directory and start Junie:

```
|  |  |
| --- | --- |
| $ | cd /path/to/your/project |
| $ | junie |
```

Type your prompt in the interactive CLI:

```
|  |
| --- |
| > give me an overview of this codebase |
```

Use `@` to attach files or folders to the request context, and type `/` to see available slash commands.

### Headless Mode (CI/CD)

Junie supports a headless mode for non-interactive use in CI/CD pipelines. Combined with OpenRouter, this gives you centralized billing and model access for automated coding tasks:

```
|  |  |
| --- | --- |
| $ | # Install Junie CLI |
| $ | curl -fsSL https://junie.jetbrains.com/install.sh | bash |
| $ |  |
| $ | # Run Junie with OpenRouter in headless mode |
| $ | export JUNIE_OPENROUTER_API_KEY="$OPENROUTER_API_KEY" |
| $ | junie "Review and fix any code quality issues in the latest commit" |
```

#### GitHub Actions Example

```
|  |  |
| --- | --- |
| 1 | name: Code Review |
| 2 | on: |
| 3 | pull_request: |
| 4 | types: [opened, synchronize] |
| 5 | jobs: |
| 6 | review: |
| 7 | runs-on: ubuntu-latest |
| 8 | permissions: |
| 9 | contents: read |
| 10 | pull-requests: write |
| 11 | issues: write |
| 12 | steps: |
| 13 | - uses: actions/checkout@v4 |
| 14 | with: |
| 15 | fetch-depth: 1 |
| 16 | - uses: JetBrains/junie-github-action@v0 |
| 17 | with: |
| 18 | openrouter_api_key: ${{ secrets.OPENROUTER_API_KEY }} |
| 19 | prompt: "code-review" |
```

#### GitLab CI/CD Example

Follow the
[setup instructions](https://junie.jetbrains.com/docs/junie-gitlab-ci-cd.html)
to configure the Junie Workspace project, then add
`JUNIE_OPENROUTER_API_KEY` as a CI/CD variable. Once
set up, trigger reviews by commenting on any MR:

```
|  |
| --- |
| #junie code-review |
```

### Verify Your Connection

After starting a session, check the [OpenRouter Activity Dashboard](https://openrouter.ai/activity) to confirm your requests are being routed through OpenRouter.

### Learn More

- **Junie CLI Documentation**: [junie.jetbrains.com/docs](https://junie.jetbrains.com/docs/junie-cli.html)
- **Junie Environment Variables**: [Environment Variables Reference](https://junie.jetbrains.com/docs/environment-variables.html)
- **OpenRouter Quick Start**: [Getting Started with OpenRouter](../../../quickstart/index.md)
- **Available Models**: [Browse OpenRouter Models](https://openrouter.ai/models)
