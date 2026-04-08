---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/bulkassignmembersrequest"
title: "BulkAssignMembersRequest Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.973501+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

BulkAssignMembersRequest - TypeScript SDK

BulkAssignMembersRequest type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { BulkAssignMembersRequest } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: BulkAssignMembersRequest = { |
| 4 | memberUserIds: [ |
| 5 | "user_abc123", |
| 6 | "user_def456", |
| 7 | ], |
| 8 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `memberUserIds` | *string*[] | ✔️ | Array of member user IDs to assign to the guardrail | [ “user\_abc123”, “user\_def456” ] |
