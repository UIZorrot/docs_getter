---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/sendchatcompletionrequestrequest"
title: "SendChatCompletionRequestRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:03.544017+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

SendChatCompletionRequestRequest - TypeScript SDK

SendChatCompletionRequestRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { SendChatCompletionRequestRequest } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: SendChatCompletionRequestRequest = { |
| 4 | chatRequest: { |
| 5 | messages: [ |
| 6 | { |
| 7 | role: "system", |
| 8 | content: "You are a helpful assistant.", |
| 9 | }, |
| 10 | { |
| 11 | role: "user", |
| 12 | content: "What is the capital of France?", |
| 13 | }, |
| 14 | ], |
| 15 | }, |
| 16 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `httpReferer` | *string* | ➖ | The app identifier should be your app’s URL and is used as the primary identifier for rankings. This is used to track API usage per application. |  |
| `appTitle` | *string* | ➖ | The app display name allows you to customize how your app appears in OpenRouter’s dashboard. |  |
| `appCategories` | *string* | ➖ | Comma-separated list of app categories (e.g. “cli-agent,cloud-agent”). Used for marketplace rankings. |  |
| `chatRequest` | [models.ChatRequest](../../models/chatrequest/index.md) | ✔️ | N/A | `{"messages": [{"role": "system","content": "You are a helpful assistant."}`, `{"role": "user","content": "What is the capital of France?"}` ], “model”: “openai/gpt-4”, “temperature”: 0.7, “max\_tokens”: `150<br />`} |
