---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/listkeyassignmentsresponse"
title: "ListKeyAssignmentsResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:15.247780+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ListKeyAssignmentsResponse - TypeScript SDK

ListKeyAssignmentsResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListKeyAssignmentsResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ListKeyAssignmentsResponse = { |
| 4 | data: [ |
| 5 | { |
| 6 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 7 | keyHash: |
| 8 | "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 9 | guardrailId: "550e8400-e29b-41d4-a716-446655440001", |
| 10 | keyName: "Production Key", |
| 11 | keyLabel: "prod-key", |
| 12 | assignedBy: "user_abc123", |
| 13 | createdAt: "2025-08-24T10:30:00Z", |
| 14 | }, |
| 15 | ], |
| 16 | totalCount: 1, |
| 17 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `data` | [models.KeyAssignment](../keyassignment/index.md)[] | ✔️ | List of key assignments |  |
| `totalCount` | *number* | ✔️ | Total number of key assignments for this guardrail | 25 |
