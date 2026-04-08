---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/textextendedconfig"
title: "TextExtendedConfig Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:19.144687+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

TextExtendedConfig - TypeScript SDK

TextExtendedConfig type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Text output configuration including format and verbosity

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { TextExtendedConfig } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: TextExtendedConfig = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `format` | *models.Formats* | ➖ | Text response format configuration | `{"type": "text"}` |
| `verbosity` | [models.TextExtendedConfigVerbosity](../textextendedconfigverbosity/index.md) | ➖ | N/A |  |
