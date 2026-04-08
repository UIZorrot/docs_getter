---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/deleteguardrailresponse"
title: "DeleteGuardrailResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:04.818733+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

DeleteGuardrailResponse - TypeScript SDK

DeleteGuardrailResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { DeleteGuardrailResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: DeleteGuardrailResponse = { |
| 4 | deleted: true, |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `deleted` | *true* | ✔️ | Confirmation that the guardrail was deleted | true |
