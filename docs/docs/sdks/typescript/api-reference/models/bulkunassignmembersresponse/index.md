---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/bulkunassignmembersresponse"
title: "BulkUnassignMembersResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:05.783312+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

BulkUnassignMembersResponse - TypeScript SDK

BulkUnassignMembersResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { BulkUnassignMembersResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: BulkUnassignMembersResponse = { |
| 4 | unassignedCount: 2, |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `unassignedCount` | *number* | ✔️ | Number of members successfully unassigned | 2 |
