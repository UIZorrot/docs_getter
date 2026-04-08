---
source_url: "https://openrouter.ai/docs/guides/coding-agents/automatic-code-review"
title: "Automatic Code Review for Claude Code | OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:32.068919+00:00"
---
[Guides](../../administration/activity-export/index.md)[Coding Agents](index.md)

# Automatic Code Review

Automatic code review for Claude Code using hooks and OpenRouter — async, non-blocking reviews from a second model while you keep working

##### 

A reference implementation is available at
[**redline**](https://github.com/alexanderatallah/redline).
Key features:

- Claude (or you) decides when a review is necessary
- Claude Code is in full control of the reviewer agent — it runs as an async background process
- Both agents are observable, customizable, and cost-monitored on [OpenRouter](https://openrouter.ai/)
- Log into both agents with one command: `redline login`
- Implemented as a single Claude Code stop hook, providing transparency and customizability on the agent and model(s) used

## What This Achieves

Every time Claude Code finishes a response and there
are uncommitted changes, a hook automatically triggers
a background Codex code review — without blocking your
workflow. You keep working while the review runs. When
it finishes, Claude reads the output and presents the
findings.

```
|  |
| --- |
| Claude Code Stop event |
| → redline check              (fast, <1s) |
| → git diff --stat HEAD       (any uncommitted changes?) |
| → hash diff stat, compare to .git/redline-last-diff |
| → if changes exist AND diff has changed since last check: |
| save hash to .git/redline-last-diff |
| output { "decision": "block", "reason": "..." } |
| reason includes diff stat summary |
| Claude decides if changes warrant a review |
| Claude spawns `redline review` as background task |
| → codex exec review streams output in real-time |
| → user can monitor, kill, or keep working |
| → when done, Claude reads output, presents findings |
| → if no changes OR same diff as last check: |
| exit 0 silently → Claude proceeds normally |
```

No background processes, no daemons, no filesystem
protocols. The hook is the trigger, and Claude Code’s
own background task system handles async execution.

## Prerequisites

- An [OpenRouter API key](https://openrouter.ai/settings/keys)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
  installed (`claude` on PATH)
- [Codex CLI](https://github.com/openai/codex)
  installed (`codex` on PATH)
- [Bun](https://bun.sh/) or Node.js runtime

## Configuring OpenRouter

Both agents route inference through OpenRouter, but
they use different API skins with different base URLs.

### Claude Code

Set these environment variables in your shell profile
(`~/.zshrc`, `~/.bashrc`). **Do not** use a `.env`
file — Claude Code doesn’t read them.

```
|  |  |
| --- | --- |
| $ | export ANTHROPIC_BASE_URL="https://openrouter.ai/api" |
| $ | export ANTHROPIC_AUTH_TOKEN="sk-or-..." |
| $ | export ANTHROPIC_API_KEY="" |
```

##### 

The base URL is `https://openrouter.ai/api` — **no
`/v1` suffix**. This is OpenRouter’s Anthropic Skin,
which speaks the native Anthropic protocol. Using
`/v1` causes model-not-found errors.
`ANTHROPIC_API_KEY` must be explicitly empty to
prevent Claude Code from authenticating directly
with Anthropic.

Verify by running `/status` in a Claude Code session.
See the full
[Claude Code integration guide](../claude-code-integration/index.md)
for details.

### Codex CLI

Create or edit `~/.codex/config.toml`:

```
|  |  |
| --- | --- |
| 1 | [model_providers.openrouter] |
| 2 | name = "openrouter" |
| 3 | base_url = "https://openrouter.ai/api/v1" |
| 4 | env_key = "OPENROUTER_API_KEY" |
```

Then set the API key:

```
|  |  |
| --- | --- |
| $ | export OPENROUTER_API_KEY="sk-or-..." |
```

At runtime, pass
`-c 'model_provider="openrouter"'` to select the
OpenRouter provider.

##### 

Common pitfalls:

- Codex CLI does **not** have a `--provider` flag —
  use `-c` for all runtime config overrides
- The TOML section is `[model_providers.openrouter]`,
  **not** `[provider.openrouter]`
- Codex uses `https://openrouter.ai/api/v1` (with
  `/v1`), while Claude uses
  `https://openrouter.ai/api` (without `/v1`) —
  they use different protocol skins

See the full
[Codex CLI integration guide](../codex-cli/index.md)
for details.

## Understanding the Stop Hook

Claude Code has a hook system configured in
`settings.json`. The key hook for this use case is
**Stop**, which fires every time Claude finishes a
response cycle.

### How `decision: "block"` works

1. The hook command runs and outputs JSON to stdout
2. If the JSON contains `"decision": "block"` with a
   `"reason"` string, Claude Code:
   - Does **not** stop — it continues the conversation
   - The `reason` text is injected into Claude’s
     context as new information
   - Claude processes it and acts on it (e.g.,
     spawning a background task as instructed)
3. If the command exits 0 with no JSON output, Claude
   proceeds normally (no blocking)
4. If the command exits non-zero, it’s treated as a
   non-blocking error

This is the key mechanism: the check command uses
`decision: "block"` to inject a diff stat summary
and review instructions into Claude’s context. Claude
sees the summary, decides whether the changes warrant
a review, and if so spawns the review command via its
Bash tool. The background task appears in Claude’s
task list — visible, monitorable, and killable.

### Settings file locations

In order of precedence:

- `~/.claude/settings.json` — global (all projects)
- `.claude/settings.json` — project (shareable,
  committed)
- `.claude/settings.local.json` — project (local,
  gitignored)

Use `.claude/settings.local.json` for the review
hook so it doesn’t affect other collaborators.

### Hook configuration

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "hooks": { |
| 3 | "Stop": [ |
| 4 | { |
| 5 | "hooks": [ |
| 6 | { |
| 7 | "type": "command", |
| 8 | "command": "redline check", |
| 9 | "timeout": 10 |
| 10 | } |
| 11 | ] |
| 12 | } |
| 13 | ] |
| 14 | } |
| 15 | } |
```

The timeout is 10 seconds — the check is fast. This
is much lower than the 300s you’d need for a
synchronous review.

## Why Async Matters

A simpler synchronous approach — running the full
review inside the Stop hook — has three problems:

1. **Blocking.** `codex exec review` can take minutes.
   A synchronous Stop hook blocks Claude Code the
   entire time — no progress visibility, no way to
   cancel.
2. **No filtering.** The hook fires after every
   response, even when Claude just answered a question
   and made no code changes.
3. **Duplicate reviews.** Nothing prevents the hook
   from triggering a second review while one is
   already running.

The async approach solves all three: the check is
fast (<1s), only fires when changes exist, hashes
the diff stat to skip when nothing has changed since
the last check, and the reason text tells Claude to
skip if a review is already running. The actual
review runs as a Claude Code background task that the
user can monitor and kill.

## The Two-Command Architecture

The tool splits into two commands: **check** (the
fast gate, called by the hook) and **review** (the
actual work, spawned by Claude as a background task).

### Building the check command

The check command runs on every Stop event and must
complete in under a second.

```
|  |  |
| --- | --- |
| 1 | import { execSync } from "child_process"; |
| 2 | import { |
| 3 | existsSync, |
| 4 | readFileSync, |
| 5 | writeFileSync, |
| 6 | } from "fs"; |
| 7 | import { join } from "path"; |
| 8 |  |
| 9 | function getDiffStat(): string { |
| 10 | // Prefer diff --stat for a concise summary |
| 11 | const diff = execSync("git diff --stat HEAD", { |
| 12 | encoding: "utf-8", |
| 13 | }).trim(); |
| 14 | if (diff) return diff; |
| 15 |  |
| 16 | // Fall back to status for untracked files |
| 17 | return execSync("git status --porcelain", { |
| 18 | encoding: "utf-8", |
| 19 | }).trim(); |
| 20 | } |
| 21 |  |
| 22 | function hash(s: string): string { |
| 23 | let h = 0; |
| 24 | for (let i = 0; i < s.length; i++) { |
| 25 | h = ((h << 5) - h + s.charCodeAt(i)) | 0; |
| 26 | } |
| 27 | return h.toString(36); |
| 28 | } |
| 29 |  |
| 30 | function check(model?: string): void { |
| 31 | const diffStat = getDiffStat(); |
| 32 | if (!diffStat) { |
| 33 | process.exit(0); |
| 34 | } |
| 35 |  |
| 36 | // Deduplicate: skip if diff unchanged since last check |
| 37 | const gitDir = execSync("git rev-parse --git-dir", { |
| 38 | encoding: "utf-8", |
| 39 | }).trim(); |
| 40 | const hashFile = join(gitDir, "redline-last-diff"); |
| 41 | const currentHash = hash(diffStat); |
| 42 |  |
| 43 | if (existsSync(hashFile)) { |
| 44 | const lastHash = readFileSync( |
| 45 | hashFile, |
| 46 | "utf-8", |
| 47 | ).trim(); |
| 48 | if (lastHash === currentHash) { |
| 49 | process.exit(0); |
| 50 | } |
| 51 | } |
| 52 |  |
| 53 | writeFileSync(hashFile, currentHash); |
| 54 |  |
| 55 | const cmd = model |
| 56 | ? `redline review --model ${model}` |
| 57 | : "redline review"; |
| 58 |  |
| 59 | const hookOutput = { |
| 60 | decision: "block", |
| 61 | reason: [ |
| 62 | "Redline: Here is a summary of uncommitted", |
| 63 | "changes since the last review:", |
| 64 | "", |
| 65 | diffStat, |
| 66 | "", |
| 67 | "If these changes are substantial enough to", |
| 68 | "warrant a code review (e.g., new logic, bug", |
| 69 | "fixes, refactors — not just formatting or", |
| 70 | "comments), run the following command as a", |
| 71 | "background task:", |
| 72 | "", |
| 73 | `  ${cmd}`, |
| 74 | "", |
| 75 | "If the changes are trivial, or a review is", |
| 76 | "already running, skip it. When a review", |
| 77 | "completes, assess the findings and inform", |
| 78 | "the user of any issues.", |
| 79 | ].join("\n"), |
| 80 | }; |
| 81 |  |
| 82 | console.log(JSON.stringify(hookOutput)); |
| 83 | } |
```

The check uses `git diff --stat HEAD` for a concise
summary of what changed, falling back to
`git status --porcelain` for untracked files. It
hashes the diff stat and stores it in
`.git/redline-last-diff` — if the diff hasn’t changed
since the last check, the hook exits silently. This
prevents the same diff from repeatedly firing the
hook. The diff stat is included in the reason text so
Claude can decide whether the changes warrant a
review.

### Building the review command

The review command is spawned by Claude as a
background task. It streams Codex output in real-time
for progress visibility, then prints a final summary.

```
|  |  |
| --- | --- |
| 1 | import { spawn } from "child_process"; |
| 2 | import { readFileSync, unlinkSync } from "fs"; |
| 3 | import { join } from "path"; |
| 4 | import { tmpdir } from "os"; |
| 5 |  |
| 6 | async function review(model?: string): Promise<void> { |
| 7 | const outputFile = join( |
| 8 | tmpdir(), |
| 9 | `redline-review-${Date.now()}.txt`, |
| 10 | ); |
| 11 |  |
| 12 | const args = [ |
| 13 | "exec", |
| 14 | "review", |
| 15 | "-c", |
| 16 | 'model_provider="openrouter"', |
| 17 | "--uncommitted", |
| 18 | "-o", |
| 19 | outputFile, |
| 20 | ]; |
| 21 |  |
| 22 | if (model) { |
| 23 | args.push("-c", `model="${model}"`); |
| 24 | } |
| 25 |  |
| 26 | // Stream output in real-time so background task |
| 27 | // shows progress |
| 28 | const exitCode = await new Promise<number>( |
| 29 | (resolve) => { |
| 30 | const proc = spawn("codex", args, { |
| 31 | cwd: process.cwd(), |
| 32 | env: process.env, |
| 33 | stdio: ["ignore", "inherit", "inherit"], |
| 34 | }); |
| 35 | proc.on("close", (code) => resolve(code ?? 1)); |
| 36 | }, |
| 37 | ); |
| 38 |  |
| 39 | // Read the final review from the -o output file |
| 40 | let review = ""; |
| 41 | try { |
| 42 | review = readFileSync(outputFile, "utf-8").trim(); |
| 43 | unlinkSync(outputFile); |
| 44 | } catch { |
| 45 | // No output file — output was already streamed |
| 46 | } |
| 47 |  |
| 48 | if (exitCode !== 0 && !review) { |
| 49 | console.error(`Codex review failed (exit ${exitCode}).`); |
| 50 | process.exit(1); |
| 51 | } |
| 52 |  |
| 53 | if (review) { |
| 54 | console.log("\n--- Review Summary ---\n"); |
| 55 | console.log(review); |
| 56 | } |
| 57 | } |
```

Key details:

- `codex exec review --uncommitted` — reviews all
  staged, unstaged, and untracked changes
- `stdio: "inherit"` — streams Codex output in
  real-time so the background task shows progress
- `-o <file>` — writes the last agent message to a
  file for reliable output capture
- `-c 'model_provider="openrouter"'` — routes
  through OpenRouter
- Optional: `-c 'model="openai/gpt-5.4-pro"'` for
  model override
- Exit code is checked — if Codex fails and produced
  no output, the tool exits with an error

### The reason text that instructs Claude

The check command’s `reason` field includes the diff
stat and lets Claude decide whether to review:

```
|  |
| --- |
| Redline: Here is a summary of uncommitted changes |
| since the last review: |
|  |
| src/commands/check.ts | 25 +++++++++++++++------ |
| src/commands/review.ts | 12 +++++----- |
| 2 files changed, 22 insertions(+), 15 deletions(-) |
|  |
| If these changes are substantial enough to warrant |
| a code review (e.g., new logic, bug fixes, refactors |
| — not just formatting or comments), run the |
| following command as a background task: |
|  |
| redline review |
|  |
| If the changes are trivial, or a review is already |
| running, skip it. When a review completes, assess |
| the findings and inform the user of any issues. |
```

Claude sees the summary, judges whether the changes
are substantive, and either spawns the review as a
background task or skips it. When the review
completes, Claude reads the streamed output and
presents the findings.

## Installing and Removing the Hook

The tool should provide commands to programmatically
install and remove the hook from
`.claude/settings.local.json`.

### Install

```
|  |  |
| --- | --- |
| $ | redline install |
```

Read `.claude/settings.local.json`, deep-merge the
Stop hook entry, and write back. Create the `.claude/`
directory if needed. Be idempotent — if the hook
already exists with the same config, skip. If it
exists with a different model, update it. Identify
your hooks by command prefix (commands starting with
`"redline"`).

The resulting file:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "hooks": { |
| 3 | "Stop": [ |
| 4 | { |
| 5 | "hooks": [ |
| 6 | { |
| 7 | "type": "command", |
| 8 | "command": "redline check", |
| 9 | "timeout": 10 |
| 10 | } |
| 11 | ] |
| 12 | } |
| 13 | ] |
| 14 | } |
| 15 | } |
```

### Remove

```
|  |  |
| --- | --- |
| $ | redline off |
```

Filter out hook entries whose `command` starts with
`"redline"`. Clean up empty arrays and objects
(remove `Stop: []` if empty, remove `hooks: {}` if
empty).

### Implementation

```
|  |  |
| --- | --- |
| 1 | import { |
| 2 | readFileSync, |
| 3 | writeFileSync, |
| 4 | mkdirSync, |
| 5 | } from "fs"; |
| 6 | import { join } from "path"; |
| 7 |  |
| 8 | const SETTINGS_PATH = join( |
| 9 | ".claude", |
| 10 | "settings.local.json", |
| 11 | ); |
| 12 | const HOOK_PREFIX = "redline"; |
| 13 |  |
| 14 | function readSettings(): Record<string, unknown> { |
| 15 | try { |
| 16 | return JSON.parse( |
| 17 | readFileSync(SETTINGS_PATH, "utf-8"), |
| 18 | ); |
| 19 | } catch { |
| 20 | return {}; |
| 21 | } |
| 22 | } |
| 23 |  |
| 24 | function writeSettings( |
| 25 | settings: Record<string, unknown>, |
| 26 | ): void { |
| 27 | mkdirSync(".claude", { recursive: true }); |
| 28 | writeFileSync( |
| 29 | SETTINGS_PATH, |
| 30 | JSON.stringify(settings, null, 2) + "\n", |
| 31 | ); |
| 32 | } |
| 33 |  |
| 34 | function installHook(model?: string): void { |
| 35 | const settings = readSettings(); |
| 36 | const command = model |
| 37 | ? `${HOOK_PREFIX} check --model ${model}` |
| 38 | : `${HOOK_PREFIX} check`; |
| 39 |  |
| 40 | const hookEntry = { |
| 41 | hooks: [ |
| 42 | { |
| 43 | type: "command", |
| 44 | command, |
| 45 | timeout: 10, |
| 46 | }, |
| 47 | ], |
| 48 | }; |
| 49 |  |
| 50 | const hooks = (settings.hooks ?? {}) as Record< |
| 51 | string, |
| 52 | unknown[] |
| 53 | >; |
| 54 | const stopHooks = (hooks.Stop ?? []) as Array<{ |
| 55 | hooks: Array<{ command: string }>; |
| 56 | }>; |
| 57 |  |
| 58 | // Check for existing redline hook |
| 59 | const existing = stopHooks.findIndex((h) => |
| 60 | h.hooks?.some((inner) => |
| 61 | inner.command?.startsWith(HOOK_PREFIX), |
| 62 | ), |
| 63 | ); |
| 64 |  |
| 65 | if (existing >= 0) { |
| 66 | stopHooks[existing] = hookEntry; |
| 67 | } else { |
| 68 | stopHooks.push(hookEntry); |
| 69 | } |
| 70 |  |
| 71 | hooks.Stop = stopHooks; |
| 72 | settings.hooks = hooks; |
| 73 | writeSettings(settings); |
| 74 | } |
| 75 |  |
| 76 | function removeHook(): void { |
| 77 | const settings = readSettings(); |
| 78 | const hooks = (settings.hooks ?? {}) as Record< |
| 79 | string, |
| 80 | unknown[] |
| 81 | >; |
| 82 | const stopHooks = (hooks.Stop ?? []) as Array<{ |
| 83 | hooks: Array<{ command: string }>; |
| 84 | }>; |
| 85 |  |
| 86 | hooks.Stop = stopHooks.filter( |
| 87 | (h) => |
| 88 | !h.hooks?.some((inner) => |
| 89 | inner.command?.startsWith(HOOK_PREFIX), |
| 90 | ), |
| 91 | ); |
| 92 |  |
| 93 | if ( |
| 94 | Array.isArray(hooks.Stop) && |
| 95 | hooks.Stop.length === 0 |
| 96 | ) { |
| 97 | delete hooks.Stop; |
| 98 | } |
| 99 | if (Object.keys(hooks).length === 0) { |
| 100 | delete settings.hooks; |
| 101 | } |
| 102 |  |
| 103 | writeSettings(settings); |
| 104 | } |
```

## Putting It Together

The full CLI has four commands:

```
|  |  |
| --- | --- |
| $ | # Install the hook |
| $ | redline install |
| $ |  |
| $ | # Install with a specific review model |
| $ | redline install --model openai/gpt-5.4-pro |
| $ |  |
| $ | # Remove the hook |
| $ | redline off |
| $ |  |
| $ | # Run a review manually (prints to stdout) |
| $ | redline review |
| $ |  |
| $ | # Fast gate check (called by the Stop hook) |
| $ | redline check |
```

### Full CLI entry point

```
|  |  |
| --- | --- |
| 1 | const args = process.argv.slice(2); |
| 2 | const command = args[0]; |
| 3 |  |
| 4 | const modelFlag = args.indexOf("--model"); |
| 5 | const model = |
| 6 | modelFlag >= 0 ? args[modelFlag + 1] : undefined; |
| 7 |  |
| 8 | switch (command) { |
| 9 | case "install": |
| 10 | installHook(model); |
| 11 | console.log( |
| 12 | "Hook installed in", |
| 13 | ".claude/settings.local.json", |
| 14 | ); |
| 15 | break; |
| 16 |  |
| 17 | case "off": |
| 18 | removeHook(); |
| 19 | console.log("Hook removed."); |
| 20 | break; |
| 21 |  |
| 22 | case "check": |
| 23 | check(model); |
| 24 | break; |
| 25 |  |
| 26 | case "review": |
| 27 | review(model); |
| 28 | break; |
| 29 |  |
| 30 | default: |
| 31 | installHook(model); |
| 32 | console.log( |
| 33 | "Hook installed in", |
| 34 | ".claude/settings.local.json", |
| 35 | ); |
| 36 | break; |
| 37 | } |
```

## Testing

### Verify hook installation

```
|  |  |
| --- | --- |
| $ | redline install |
| $ | cat .claude/settings.local.json |
```

You should see the Stop hook entry with the
`redline check` command and a 10-second timeout.

### Test check with no changes

Ensure your working tree is clean, then:

```
|  |  |
| --- | --- |
| $ | redline check |
```

No output — the check exits silently when there are
no uncommitted changes.

### Test check with changes

Make a small change to any file, then:

```
|  |  |
| --- | --- |
| $ | redline check |
```

You should see JSON with `"decision": "block"` and a
`"reason"` containing the diff stat summary and
review instructions.

### Test review

```
|  |  |
| --- | --- |
| $ | redline review |
```

You should see streamed Codex output followed by a
review summary.

### Full integration test

1. Install the hook: `redline install`
2. Start Claude Code: `claude`
3. Ask Claude to make a small code change
4. When Claude finishes, the Stop hook fires the
   check — if there are uncommitted changes, Claude
   spawns the review as a background task
5. You can keep working while the review runs
6. When the review completes, Claude reads the output
   and presents any findings

## Limitations and Future Work

### Claude Code only

This pattern relies on Claude Code’s
`decision: "block"` hook output, which injects
instructions directly into the agent’s conversation.
Codex CLI’s hook system (as of early 2026) is more
limited — its `Stop` hook is fire-and-forget and
cannot feed structured output back into the model’s
context. Native hooks (`[[hooks]]` in config.toml)
support several events, but only `SessionStart` can
feed stdout into the model. There is no equivalent of
`decision: "block"` + `reason` for injecting
mid-session instructions. When Codex adds full
structured hook output support, this pattern can be
extended.

### Review granularity

The review covers everything uncommitted — all
staged, unstaged, and untracked changes. It does not
distinguish between changes Claude just made and
pre-existing uncommitted work. Future versions could
use smarter change detection (e.g., diffing against a
baseline snapshot taken before Claude’s response).

## Resources

- [Reference implementation (redline)](https://github.com/alexanderatallah/redline)
- [Claude Code integration](../claude-code-integration/index.md)
- [Codex CLI integration](../codex-cli/index.md)
- [OpenRouter Activity Dashboard](https://openrouter.ai/activity)
