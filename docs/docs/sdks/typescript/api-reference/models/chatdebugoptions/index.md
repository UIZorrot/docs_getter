---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/chatdebugoptions"
title: "ChatDebugOptions Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.510766+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ChatDebugOptions - TypeScript SDK

ChatDebugOptions type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Debug options for inspecting request transformations (streaming only)

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ChatDebugOptions } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ChatDebugOptions = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `echoUpstreamBody` | *boolean* | ➖ | If true, includes the transformed upstream request body in a debug chunk at the start of the stream. Only works with streaming mode. | true |
