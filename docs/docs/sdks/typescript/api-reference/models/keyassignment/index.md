---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/keyassignment"
title: "KeyAssignment Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.850178+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

KeyAssignment - TypeScript SDK

KeyAssignment type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { KeyAssignment } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: KeyAssignment = { |
| 4 | id: "550e8400-e29b-41d4-a716-446655440000", |
| 5 | keyHash: "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93", |
| 6 | guardrailId: "550e8400-e29b-41d4-a716-446655440001", |
| 7 | keyName: "Production Key", |
| 8 | keyLabel: "prod-key", |
| 9 | assignedBy: "user_abc123", |
| 10 | createdAt: "2025-08-24T10:30:00Z", |
| 11 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *string* | ✔️ | Unique identifier for the assignment | 550e8400-e29b-41d4-a716-446655440000 |
| `keyHash` | *string* | ✔️ | Hash of the assigned API key | c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93 |
| `guardrailId` | *string* | ✔️ | ID of the guardrail | 550e8400-e29b-41d4-a716-446655440001 |
| `keyName` | *string* | ✔️ | Name of the API key | Production Key |
| `keyLabel` | *string* | ✔️ | Label of the API key | prod-key |
| `assignedBy` | *string* | ✔️ | User ID of who made the assignment | user\_abc123 |
| `createdAt` | *string* | ✔️ | ISO 8601 timestamp of when the assignment was created | 2025-08-24T10:30:00Z |
