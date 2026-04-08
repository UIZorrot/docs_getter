---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/architecture"
title: "Architecture Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:18.345411+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

Architecture - TypeScript SDK

Architecture type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Model architecture information

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { Architecture } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: Architecture = { |
| 4 | tokenizer: "GPT", |
| 5 | instructType: "chatml", |
| 6 | modality: "text", |
| 7 | inputModalities: [ |
| 8 | "text", |
| 9 | ], |
| 10 | outputModalities: [ |
| 11 | "text", |
| 12 | ], |
| 13 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `tokenizer` | [models.Tokenizer](../tokenizer/index.md) | ✔️ | N/A | GPT |
| `instructType` | [models.InstructType](../instructtype/index.md) | ✔️ | Instruction format type | chatml |
| `modality` | *string* | ✔️ | Primary modality of the model | text |
| `inputModalities` | [models.InputModality](../inputmodality/index.md)[] | ✔️ | Supported input modalities |  |
| `outputModalities` | [models.OutputModality](../outputmodality/index.md)[] | ✔️ | Supported output modalities |  |
