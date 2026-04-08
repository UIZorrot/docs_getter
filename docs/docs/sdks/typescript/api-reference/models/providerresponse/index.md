---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/providerresponse"
title: "ProviderResponse Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.164024+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ProviderResponse - TypeScript SDK

ProviderResponse type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

Details of a provider response for a generation attempt

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ProviderResponse } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ProviderResponse = { |
| 4 | status: 200, |
| 5 | }; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `id` | *string* | ➖ | Upstream provider response identifier | chatcmpl-abc123 |
| `endpointId` | *string* | ➖ | Internal endpoint identifier | ep\_abc123 |
| `modelPermaslug` | *string* | ➖ | Canonical model slug | openai/gpt-4 |
| `providerName` | [models.ProviderResponseProviderName](../providerresponseprovidername/index.md) | ➖ | Name of the provider | OpenAI |
| `status` | *number* | ✔️ | HTTP status code from the provider | 200 |
| `latency` | *number* | ➖ | Response latency in milliseconds | 1200 |
| `isByok` | *boolean* | ➖ | Whether the request used a bring-your-own-key | false |
