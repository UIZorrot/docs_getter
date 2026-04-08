---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/anthropiccachecontroldirective"
title: "AnthropicCacheControlDirective Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.575747+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

AnthropicCacheControlDirective - TypeScript SDK

AnthropicCacheControlDirective type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Enable automatic prompt caching. When set, the system automatically applies cache breakpoints to the last cacheable block in the request. Currently supported for Anthropic Claude models.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { AnthropicCacheControlDirective } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: AnthropicCacheControlDirective = { |
| 4 | type: "ephemeral", |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `type` | [models.AnthropicCacheControlDirectiveType](../anthropiccachecontroldirectivetype/index.md) | ✔️ | N/A |  |
| `ttl` | [models.AnthropicCacheControlTtl](../anthropiccachecontrolttl/index.md) | ➖ | N/A | 5m |
