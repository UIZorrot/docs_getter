---
source_url: "https://openrouter.ai/docs/guides/features/server-tools/datetime"
title: "Datetime Server Tool | Current Date and Time for Any Model | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:38.507588+00:00"
---
[Features](../../presets/index.md)[Server Tools](../overview/index.md)

# Datetime

Beta

Give any model access to the current date and time

##### Beta

Server tools are currently in beta. The API and behavior may change.

The `openrouter:datetime` server tool gives any model access to the current date and time. This is useful for prompts that require temporal awareness — scheduling, time-sensitive questions, or any task where the model needs to know “right now.”

## Quick Start

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/chat/completions', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | Authorization: 'Bearer {{API_KEY_REF}}', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: '{{MODEL}}', |
| 9 | messages: [ |
| 10 | { |
| 11 | role: 'user', |
| 12 | content: 'What day of the week is it today?' |
| 13 | } |
| 14 | ], |
| 15 | tools: [ |
| 16 | { type: 'openrouter:datetime' } |
| 17 | ] |
| 18 | }), |
| 19 | }); |
| 20 |  |
| 21 | const data = await response.json(); |
| 22 | console.log(data.choices[0].message.content); |
```

## Configuration

The datetime tool accepts an optional `timezone` parameter:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "type": "openrouter:datetime", |
| 3 | "parameters": { |
| 4 | "timezone": "America/New_York" |
| 5 | } |
| 6 | } |
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `timezone` | string | `UTC` | IANA timezone name (e.g. `"America/New_York"`, `"Europe/London"`, `"Asia/Tokyo"`) |

## Response

When the model calls the datetime tool, it receives a response like:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "datetime": "2025-07-15T14:30:00.000-04:00", |
| 3 | "timezone": "America/New_York" |
| 4 | } |
```

## Pricing

The datetime tool has no additional cost beyond standard token usage.

## Next Steps

- [Server Tools Overview](../index.md) — Learn about server tools
- [Web Search](../web-search/index.md) — Search the web for real-time information
- [Tool Calling](../../tool-calling/index.md) — Learn about user-defined tool calling
