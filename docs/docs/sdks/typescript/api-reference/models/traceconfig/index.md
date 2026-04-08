---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/traceconfig"
title: "TraceConfig Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.112135+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

TraceConfig - TypeScript SDK

TraceConfig type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Metadata for observability and tracing. Known keys (trace\_id, trace\_name, span\_name, generation\_name, parent\_span\_id) have special handling. Additional keys are passed through as custom metadata to configured broadcast destinations.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { TraceConfig } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: TraceConfig = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `traceId` | *string* | ➖ | N/A |  |
| `traceName` | *string* | ➖ | N/A |  |
| `spanName` | *string* | ➖ | N/A |  |
| `generationName` | *string* | ➖ | N/A |  |
| `parentSpanId` | *string* | ➖ | N/A |  |
| `additionalProperties` | `Record<string, *any*>` | ➖ | N/A | `{"trace_id": "trace-abc123","trace_name": "my-app-trace"}` |
