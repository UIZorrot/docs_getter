---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/chatrequestservicetier"
title: "ChatRequestServiceTier Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.701142+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ChatRequestServiceTier - TypeScript SDK

ChatRequestServiceTier type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

The service tier to use for processing this request.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ChatRequestServiceTier } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ChatRequestServiceTier = "auto"; |
| 4 |  |
| 5 | // Open enum: unrecognized values are captured as Unrecognized<string> |
```

## Values

```
|  |  |
| --- | --- |
| 1 | "auto" | "default" | "flex" | "priority" | "scale" | Unrecognized<string> |
```
