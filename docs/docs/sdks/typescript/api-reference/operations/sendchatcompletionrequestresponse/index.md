---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/sendchatcompletionrequestresponse"
title: "SendChatCompletionRequestResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:03.680964+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

SendChatCompletionRequestResponse - TypeScript SDK

SendChatCompletionRequestResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Supported Types

### `models.ChatResult`

```
|  |  |
| --- | --- |
| 1 | const value: models.ChatResult = { |
| 2 | id: "chatcmpl-123", |
| 3 | choices: [ |
| 4 | { |
| 5 | finishReason: "stop", |
| 6 | index: 0, |
| 7 | message: { |
| 8 | role: "assistant", |
| 9 | }, |
| 10 | }, |
| 11 | ], |
| 12 | created: 1677652288, |
| 13 | model: "openai/gpt-4", |
| 14 | object: "chat.completion", |
| 15 | systemFingerprint: "fp_44709d6fcb", |
| 16 | }; |
```

### `EventStream<operations.SendChatCompletionRequestResponseBody>`
