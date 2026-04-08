---
source_url: "https://openrouter.ai/docs/guides/features/service-tiers"
title: "Service Tiers | OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:38.745820+00:00"
---
[Features](../presets/index.md)

# Service Tiers

Control cost and latency tradeoffs with service tier selection

## Service Tiers

The `service_tier` parameter lets you control cost and latency tradeoffs when sending requests through OpenRouter. You can pass it in your request to select a specific processing tier, and the response will indicate which tier was actually used.

### Supported Providers

**OpenAI**

Accepted request values: `auto`, `default`, `flex`, `priority`

Learn more in OpenAI’s [Chat Completions](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create) and [Responses](https://developers.openai.com/api/reference/resources/responses/methods/create) API documentation. See OpenAI’s [pricing page](https://developers.openai.com/api/docs/pricing) for details on cost differences between tiers.

### API Response Differences

The API response includes a `service_tier` field that indicates which capacity tier was actually used to serve your request. The placement of this field varies by API format:

- **Chat Completions API** (`/api/v1/chat/completions`): `service_tier` is returned at the **top level** of the response object, matching OpenAI’s native format.
- **Responses API** (`/api/v1/responses`): `service_tier` is returned at the **top level** of the response object, matching OpenAI’s native format.
- **Messages API** (`/api/v1/messages`): `service_tier` is returned inside the **`usage` object**, matching Anthropic’s native format.
