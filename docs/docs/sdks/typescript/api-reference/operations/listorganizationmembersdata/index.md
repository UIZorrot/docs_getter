---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listorganizationmembersdata"
title: "ListOrganizationMembersData Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:18.881105+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListOrganizationMembersData - TypeScript SDK

ListOrganizationMembersData type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListOrganizationMembersData } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListOrganizationMembersData = { |
| 4 | id: "user_2dHFtVWx2n56w6HkM0000000000", |
| 5 | firstName: "Jane", |
| 6 | lastName: "Doe", |
| 7 | email: "jane.doe@example.com", |
| 8 | role: "org:member", |
| 9 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *string* | ✔️ | User ID of the organization member | user\_2dHFtVWx2n56w6HkM0000000000 |
| `firstName` | *string* | ✔️ | First name of the member | Jane |
| `lastName` | *string* | ✔️ | Last name of the member | Doe |
| `email` | *string* | ✔️ | Email address of the member | [jane.doe@example.com](mailto:jane.doe@example.com) |
| `role` | [operations.Role](../role/index.md) | ✔️ | Role of the member in the organization | org:member |
