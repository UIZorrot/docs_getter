---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/operations/listprovidersdata"
title: "ListProvidersData Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:16.850313+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)Operations

# 

ListProvidersData - TypeScript SDK

ListProvidersData type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ListProvidersData } from "@openrouter/sdk/models/operations"; |
| 2 |  |
| 3 | let value: ListProvidersData = { |
| 4 | name: "OpenAI", |
| 5 | slug: "openai", |
| 6 | privacyPolicyUrl: "https://openai.com/privacy", |
| 7 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `name` | *string* | ✔️ | Display name of the provider | OpenAI |
| `slug` | *string* | ✔️ | URL-friendly identifier for the provider | openai |
| `privacyPolicyUrl` | *string* | ✔️ | URL to the provider’s privacy policy | [https://openai.com/privacy](https://openai.com/privacy) |
| `termsOfServiceUrl` | *string* | ➖ | URL to the provider’s terms of service | [https://openai.com/terms](https://openai.com/terms) |
| `statusPageUrl` | *string* | ➖ | URL to the provider’s status page | [https://status.openai.com](https://status.openai.com/) |
| `headquarters` | [operations.Headquarters](../headquarters/index.md) | ➖ | ISO 3166-1 Alpha-2 country code of the provider headquarters | US |
| `datacenters` | [operations.Datacenter](../datacenter/index.md)[] | ➖ | ISO 3166-1 Alpha-2 country codes of the provider datacenter locations | [ “US”, “IE” ] |
