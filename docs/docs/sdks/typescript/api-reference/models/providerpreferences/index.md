---
source_url: "https://openrouter.ai/docs/sdks/typescript/api-reference/models/providerpreferences"
title: "ProviderPreferences Type | OpenRouter TypeScript SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:30:17.326521+00:00"
---
[TypeScript SDK](../../../overview/index.md)[API Reference](../../analytics/index.md)[Models](../models/index.md)

# 

ProviderPreferences - TypeScript SDK

ProviderPreferences type definition

##### 

The TypeScript SDK and docs are currently in beta.
Report issues on [GitHub](https://github.com/OpenRouterTeam/typescript-sdk/issues).

When multiple model providers are available, optionally indicate your routing preference.

## Example Usage

```
|  |  |
| --- | --- |
| 1 | import { ProviderPreferences } from "@openrouter/sdk/models"; |
| 2 |  |
| 3 | let value: ProviderPreferences = {}; |
```

## Fields

| Field | Type | Required | Description | Example |
| --- | --- | --- | --- | --- |
| `allowFallbacks` | *boolean* | ➖ | Whether to allow backup providers to serve `requests<br />`- true: (default) when the primary provider (or your custom providers in “order”) is unavailable, use the next best provider. - false: use only the primary/custom provider, and return the upstream error if it’s unavailable. |  |
| `requireParameters` | *boolean* | ➖ | Whether to filter providers to only those that support the parameters you’ve provided. If this setting is omitted or set to false, then providers will receive only the parameters they support, and ignore the rest. |  |
| `dataCollection` | [models.DataCollection](../datacollection/index.md) | ➖ | Data collection setting. If no available model provider meets the requirement, your request will return an error. - allow: (default) allow providers which store user data non-transiently and may train on `it<br />` - deny: use only providers which do not collect user data. | allow |
| `zdr` | *boolean* | ➖ | Whether to restrict routing to only ZDR (Zero Data Retention) endpoints. When true, only endpoints that do not retain prompts will be used. | true |
| `enforceDistillableText` | *boolean* | ➖ | Whether to restrict routing to only models that allow text distillation. When true, only models where the author has allowed distillation will be used. | true |
| `order` | *models.Order*[] | ➖ | An ordered list of provider slugs. The router will attempt to use the first provider in the subset of this list that supports your requested model, and fall back to the next if it is unavailable. If no providers are available, the request will fail with an error message. | [ “openai”, “anthropic” ] |
| `only` | *models.Only*[] | ➖ | List of provider slugs to allow. If provided, this list is merged with your account-wide allowed provider settings for this request. | [ “openai”, “anthropic” ] |
| `ignore` | *models.Ignore*[] | ➖ | List of provider slugs to ignore. If provided, this list is merged with your account-wide ignored provider settings for this request. | [ “openai”, “anthropic” ] |
| `quantizations` | [models.Quantization](../quantization/index.md)[] | ➖ | A list of quantization levels to filter the provider by. |  |
| `sort` | *models.Sort* | ➖ | The sorting strategy to use for this request, if “order” is not specified. When set, no load balancing is performed. | price |
| `maxPrice` | [models.MaxPrice](../maxprice/index.md) | ➖ | The object specifying the maximum price you want to pay for this request. USD price per million tokens, for prompt and completion. |  |
| `preferredMinThroughput` | *models.PreferredMinThroughput* | ➖ | Preferred minimum throughput (in tokens per second). Can be a number (applies to p50) or an object with percentile-specific cutoffs. Endpoints below the threshold(s) may still be used, but are deprioritized in routing. When using fallback models, this may cause a fallback model to be used instead of the primary model if it meets the threshold. | 100 |
| `preferredMaxLatency` | *models.PreferredMaxLatency* | ➖ | Preferred maximum latency (in seconds). Can be a number (applies to p50) or an object with percentile-specific cutoffs. Endpoints above the threshold(s) may still be used, but are deprioritized in routing. When using fallback models, this may cause a fallback model to be used instead of the primary model if it meets the threshold. | 5 |
