---
source_url: "https://openrouter.ai/docs/sdks/agent-migration"
title: "Migrate to @openrouter/agent | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:42.269396+00:00"
---
# 

Migrating to @openrouter/agent

Move agent toolkit imports from @openrouter/sdk to the standalone @openrouter/agent package

##### 

Using an AI coding assistant? Install the migration skill
to let your agent handle the import updates for you:
`npx skills add OpenRouterTeam/skills/openrouter-agent-migration`

The agent toolkit (`callModel`, `tool`, stop conditions, etc.)
has moved from `@openrouter/sdk` to a standalone
**`@openrouter/agent`** package. The agent package includes
its own `OpenRouter` client class, so you no longer need
`@openrouter/sdk` as a dependency for agent workflows.

## Who needs to migrate?

You need to migrate if your code imports any of the following
from `@openrouter/sdk`:

- `callModel` / `ModelResult`
- `tool` / `Tool` / tool type guards
- Stop conditions (`stepCountIs`, `hasToolCall`, etc.)
- Async parameters (`CallModelInput`, `resolveAsyncFunctions`)
- Conversation state helpers
- Message format converters (`fromClaudeMessages`,
  `fromChatMessages`, etc.)

If you only use the REST API client for non-agent features
(`client.chat.send(...)`, `client.models.list()`, etc.),
**no changes are needed**.

## Step 1: Install the new package

```
|  |  |
| --- | --- |
| $ | npm install @openrouter/agent |
```

## Step 2: Update imports

Replace `@openrouter/sdk` subpath imports with
the equivalent `@openrouter/agent` subpath.

### Client class

`@openrouter/agent` ships its own `OpenRouter` client, so
you can drop the `@openrouter/sdk` dependency entirely if
you only use agent features:

```
|  |  |
| --- | --- |
| 1 | - import OpenRouter from '@openrouter/sdk'; |
| 2 | - import { callModel } from '@openrouter/sdk/funcs/call-model'; |
| 3 | + import { OpenRouter } from '@openrouter/agent'; |
| 4 |  |
| 5 | const client = new OpenRouter({ |
| 6 | apiKey: process.env.OPENROUTER_API_KEY, |
| 7 | }); |
| 8 | + |
| 9 | + const result = client.callModel({ |
| 10 | +   model: 'openai/gpt-4o', |
| 11 | +   input: 'Hello', |
| 12 | + }); |
| 13 | + const text = await result.getText(); |
```

You can also import the client from a direct subpath:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/agent/client'; |
```

### Core imports

```
|  |  |
| --- | --- |
| 1 | - import { callModel } from '@openrouter/sdk/funcs/call-model'; |
| 2 | + import { callModel } from '@openrouter/agent/call-model'; |
| 3 |  |
| 4 | - import { ModelResult } from '@openrouter/sdk/lib/model-result'; |
| 5 | + import { ModelResult } from '@openrouter/agent/model-result'; |
| 6 |  |
| 7 | - import { tool } from '@openrouter/sdk/lib/tool'; |
| 8 | + import { tool } from '@openrouter/agent/tool'; |
```

### Tool types and guards

```
|  |  |
| --- | --- |
| 1 | - import type { Tool } from '@openrouter/sdk/lib/tool-types'; |
| 2 | + import type { Tool } from '@openrouter/agent/tool-types'; |
| 3 |  |
| 4 | - import { |
| 5 | -   hasExecuteFunction, |
| 6 | -   isGeneratorTool, |
| 7 | - } from '@openrouter/sdk/lib/tool-types'; |
| 8 | + import { |
| 9 | +   hasExecuteFunction, |
| 10 | +   isGeneratorTool, |
| 11 | + } from '@openrouter/agent/tool-types'; |
```

### Stop conditions

```
|  |  |
| --- | --- |
| 1 | - import { |
| 2 | -   stepCountIs, |
| 3 | -   hasToolCall, |
| 4 | -   maxCost, |
| 5 | - } from '@openrouter/sdk/lib/stop-conditions'; |
| 6 | + import { |
| 7 | +   stepCountIs, |
| 8 | +   hasToolCall, |
| 9 | +   maxCost, |
| 10 | + } from '@openrouter/agent/stop-conditions'; |
```

### Async parameters

```
|  |  |
| --- | --- |
| 1 | - import type { |
| 2 | -   CallModelInput, |
| 3 | - } from '@openrouter/sdk/lib/async-params'; |
| 4 | + import type { |
| 5 | +   CallModelInput, |
| 6 | + } from '@openrouter/agent/async-params'; |
```

### Conversation state and message formats

Conversation helpers and message format converters are
available from the package barrel:

```
|  |  |
| --- | --- |
| 1 | - import { |
| 2 | -   createInitialState, |
| 3 | -   updateState, |
| 4 | -   fromClaudeMessages, |
| 5 | -   fromChatMessages, |
| 6 | - } from '@openrouter/sdk'; |
| 7 | + import { |
| 8 | +   createInitialState, |
| 9 | +   updateState, |
| 10 | +   fromClaudeMessages, |
| 11 | +   fromChatMessages, |
| 12 | + } from '@openrouter/agent'; |
```

## Step 3: Verify your build

Run your type checker and tests to confirm everything
resolves correctly:

```
|  |  |
| --- | --- |
| $ | npx tsc --noEmit |
| $ | npm test |
```

## Full import mapping reference

| Old import path | New import path |
| --- | --- |
| `@openrouter/sdk` (client class) | `@openrouter/agent` or `@openrouter/agent/client` |
| `@openrouter/sdk/funcs/call-model` | `@openrouter/agent/call-model` |
| `@openrouter/sdk/lib/model-result` | `@openrouter/agent/model-result` |
| `@openrouter/sdk/lib/tool` | `@openrouter/agent/tool` |
| `@openrouter/sdk/lib/tool-types` | `@openrouter/agent/tool-types` |
| `@openrouter/sdk/lib/stop-conditions` | `@openrouter/agent/stop-conditions` |
| `@openrouter/sdk/lib/async-params` | `@openrouter/agent/async-params` |
| `@openrouter/sdk` (barrel: state, messages) | `@openrouter/agent` |

## Automated migration

The script below handles **subpath imports** automatically.
Barrel imports (`from '@openrouter/sdk'`) and client class
imports (`import OpenRouter from '@openrouter/sdk'`) must
be updated **manually** — a blanket replacement on the bare
package name would also match subpath imports and break
your code. See the [Client class](#client-class) and
[Conversation state](#conversation-state-and-message-formats)
sections above for the correct replacements.

```
|  |  |
| --- | --- |
| $ | # Using sed (macOS) |
| $ | find src -name '*.ts' -o -name '*.tsx' | xargs sed -i '' \ |
| > | -e "s|@openrouter/sdk/funcs/call-model|@openrouter/agent/call-model|g" \ |
| > | -e "s|@openrouter/sdk/lib/model-result|@openrouter/agent/model-result|g" \ |
| > | -e "s|@openrouter/sdk/lib/tool-types|@openrouter/agent/tool-types|g" \ |
| > | -e "s|@openrouter/sdk/lib/tool|@openrouter/agent/tool|g" \ |
| > | -e "s|@openrouter/sdk/lib/stop-conditions|@openrouter/agent/stop-conditions|g" \ |
| > | -e "s|@openrouter/sdk/lib/async-params|@openrouter/agent/async-params|g" |
```

```
|  |  |
| --- | --- |
| $ | # Using sed (Linux) |
| $ | find src -name '*.ts' -o -name '*.tsx' | xargs sed -i \ |
| > | -e "s|@openrouter/sdk/funcs/call-model|@openrouter/agent/call-model|g" \ |
| > | -e "s|@openrouter/sdk/lib/model-result|@openrouter/agent/model-result|g" \ |
| > | -e "s|@openrouter/sdk/lib/tool-types|@openrouter/agent/tool-types|g" \ |
| > | -e "s|@openrouter/sdk/lib/tool|@openrouter/agent/tool|g" \ |
| > | -e "s|@openrouter/sdk/lib/stop-conditions|@openrouter/agent/stop-conditions|g" \ |
| > | -e "s|@openrouter/sdk/lib/async-params|@openrouter/agent/async-params|g" |
```

##### 

The `tool-types` replacement runs before `tool` to avoid
partial matches. After running the script, search your
codebase for any remaining `from '@openrouter/sdk'` (without
a `/` subpath) to find barrel and client imports that need
manual updates.

## FAQ

### Do I still need `@openrouter/sdk`?

Only if you use non-agent REST API features like
`client.models.list()`, `client.credits.get()`, or
`client.chat.send()`. If your code only uses `callModel`,
tools, and the agent client, you can remove
`@openrouter/sdk` entirely.

### Can I use both packages together?

Yes. They are designed to work side by side. Use
`@openrouter/sdk` for REST API features and
`@openrouter/agent` for the agent toolkit:

```
|  |  |
| --- | --- |
| 1 | import OpenRouter from '@openrouter/sdk'; |
| 2 | import { callModel } from '@openrouter/agent/call-model'; |
| 3 | import { tool } from '@openrouter/agent/tool'; |
```

### Will the old imports keep working?

The agent exports will be removed from `@openrouter/sdk`
in a future major version. Update your imports now to
avoid a breaking change later.

### Do I need to change my API key or configuration?

No. `@openrouter/agent` uses the same API key and
endpoints. No server-side changes are required.
