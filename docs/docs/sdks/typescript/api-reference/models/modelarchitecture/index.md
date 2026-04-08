---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/modelarchitecture"
title: "ModelArchitecture Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:18.474939+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ModelArchitecture - TypeScript SDK

ModelArchitecture type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Model architecture information

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ModelArchitecture } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ModelArchitecture = { |
| 4 | modality: "text->text", |
| 5 | inputModalities: [ |
| 6 | "text", |
| 7 | ], |
| 8 | outputModalities: [ |
| 9 | "text", |
| 10 | ], |
| 11 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `tokenizer` | [models.ModelGroup](../modelgroup/index.md) | ➖ | Tokenizer type used by the model | GPT |
| `instructType` | [models.ModelArchitectureInstructType](../modelarchitectureinstructtype/index.md) | ➖ | Instruction format type | chatml |
| `modality` | *string* | ✔️ | Primary modality of the model | text->text |
| `inputModalities` | [models.InputModality](../inputmodality/index.md)[] | ✔️ | Supported input modalities |  |
| `outputModalities` | [models.OutputModality](../outputmodality/index.md)[] | ✔️ | Supported output modalities |  |
