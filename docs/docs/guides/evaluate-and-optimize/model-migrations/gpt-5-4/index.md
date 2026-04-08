---
source_url: "https://openrouter.ai/docs/guides/evaluate-and-optimize/model-migrations/gpt-5-4"
title: "GPT-5.4 Migration Guide | OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:35.848516+00:00"
---
[Guides](../../../administration/activity-export/index.md)[Evaluate & Optimize](../../distillation/index.md)[Model Migrations](../claude-4-6/index.md)

# 

GPT-5.4 Migration Guide

Support the phase field for GPT-5.3 Codex, GPT-5.4, and GPT-5.4 Pro

## What’s New

GPT-5.4, GPT-5.4 Pro, and GPT-5.3 Codex introduce the
`phase` field on
assistant messages. This field is critical for multi-turn
agentic workflows — it tells the model whether an assistant
message is intermediate commentary or the final answer.

OpenRouter supports `phase` in the
[Responses API](../../../../api/api-reference/responses/create-responses/index.md).

##### 

`phase` is **not available** in the Chat Completions API.
The Chat Completions format cannot represent multiple
output items with distinct phases in a single response.
Use the Responses API for full `phase` support.

## The `phase` Field

`phase` appears on assistant output messages and has three
possible values:

| Value | Meaning |
| --- | --- |
| `null` | No phase specified (default) |
| `"commentary"` | Intermediate assistant message |
| `"final_answer"` | The final closeout message |

##### 

`phase` is only valid on **assistant** messages.
Do not add `phase` to user or system messages.

## Why It Matters

For models like `gpt-5.3-codex`, `gpt-5.4`, and
`gpt-5.4-pro`, correctly
preserving `phase` on assistant messages is **required**
for optimal performance. If `phase` metadata is dropped
when reconstructing conversation history, significant
performance degradation can occur — including early
stopping on longer-running tasks.

## Usage

### Responses API

When using the Responses API, assistant output items
include `phase`. You must persist these items verbatim
and pass them back in subsequent requests.

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.4", |
| 3 | "input": [ |
| 4 | { |
| 5 | "type": "message", |
| 6 | "role": "user", |
| 7 | "content": [ |
| 8 | { |
| 9 | "type": "input_text", |
| 10 | "text": "Refactor the auth module" |
| 11 | } |
| 12 | ] |
| 13 | } |
| 14 | ] |
| 15 | } |
```

The response will include `phase` on assistant output
messages:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "output": [ |
| 3 | { |
| 4 | "type": "message", |
| 5 | "role": "assistant", |
| 6 | "content": [ |
| 7 | { |
| 8 | "type": "output_text", |
| 9 | "text": "I'll start by analyzing..." |
| 10 | } |
| 11 | ], |
| 12 | "phase": "commentary" |
| 13 | }, |
| 14 | { |
| 15 | "type": "message", |
| 16 | "role": "assistant", |
| 17 | "content": [ |
| 18 | { |
| 19 | "type": "output_text", |
| 20 | "text": "Here's the refactored code..." |
| 21 | } |
| 22 | ], |
| 23 | "phase": "final_answer" |
| 24 | } |
| 25 | ] |
| 26 | } |
```

For follow-up requests, include the assistant output
items with their `phase` intact:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.4", |
| 3 | "input": [ |
| 4 | { |
| 5 | "type": "message", |
| 6 | "role": "user", |
| 7 | "content": [ |
| 8 | { |
| 9 | "type": "input_text", |
| 10 | "text": "Refactor the auth module" |
| 11 | } |
| 12 | ] |
| 13 | }, |
| 14 | { |
| 15 | "type": "message", |
| 16 | "role": "assistant", |
| 17 | "content": [ |
| 18 | { |
| 19 | "type": "output_text", |
| 20 | "text": "I'll start by analyzing..." |
| 21 | } |
| 22 | ], |
| 23 | "phase": "commentary" |
| 24 | }, |
| 25 | { |
| 26 | "type": "message", |
| 27 | "role": "assistant", |
| 28 | "content": [ |
| 29 | { |
| 30 | "type": "output_text", |
| 31 | "text": "Here's the refactored code..." |
| 32 | } |
| 33 | ], |
| 34 | "phase": "final_answer" |
| 35 | }, |
| 36 | { |
| 37 | "type": "message", |
| 38 | "role": "user", |
| 39 | "content": [ |
| 40 | { |
| 41 | "type": "input_text", |
| 42 | "text": "Now add unit tests" |
| 43 | } |
| 44 | ] |
| 45 | } |
| 46 | ] |
| 47 | } |
```

### Chat Completions API

The Chat Completions API does **not** support `phase` in
responses. A single chat completion response can only
contain one message per choice, so there is no way to
represent the separate commentary and final answer output
items that models like GPT-5.4 produce.

If you need `phase` support for multi-turn agentic
workflows, use the
[Responses API](../../../../api/api-reference/responses/create-responses/index.md)
instead.

## Implementation Pattern

When building an integration with the Responses API,
persist your output items verbatim, including `phase`
on assistant messages:

### Key Rules

1. **Preserve phase on assistant messages** — When you
   receive a response with `phase`, store it and send
   it back on subsequent requests.
2. **Do not add phase to user messages** — `phase` is
   only valid on assistant messages. The Responses API
   will reject requests with `phase` on user messages.
3. **Do not drop phase** — Omitting `phase` from
   assistant messages in multi-turn conversations will
   degrade model performance.
4. **Use the Responses API** — `phase` requires the
   Responses API. The Chat Completions API cannot
   represent multi-phase output.

## Supported Models

| Model | `phase` Support |
| --- | --- |
| `openai/gpt-5.4` | Supported |
| `openai/gpt-5.4-pro` | Supported |
| `openai/gpt-5.3-codex` | Supported |
| Other OpenAI models | Silently ignored (safe to pass) |
| Non-OpenAI models | Not applicable |

##### 

Passing `phase` to OpenAI models that don’t support it
(like `gpt-4o`) is safe — OpenAI silently ignores the
field. You do not need to filter `phase` based on the
model.

## Breaking Changes

None. The `phase` field is additive:

- Existing requests without `phase` continue to work
  on all models
- Models that don’t support `phase` silently ignore it
- No changes are required unless you want to take
  advantage of improved multi-turn performance with
  GPT-5.3 Codex, GPT-5.4, and GPT-5.4 Pro

## Resources

- [Prompt Guidance for GPT-5.4](https://developers.openai.com/api/docs/guides/prompt-guidance) — OpenAI’s official guide covering prompt patterns and migration tips for GPT-5.4, including completeness checks, verification loops, tool persistence, and structured outputs.
- [OpenAI Responses API Reference](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [Codex CLI Integration Guide](../../../coding-agents/codex-cli/index.md)
- [OpenRouter API Documentation](../../../../api/reference/overview/index.md)
- [OpenRouter Codex Models](https://openrouter.ai/models)
