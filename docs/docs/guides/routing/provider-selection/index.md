---
source_url: "https://openrouter.ai/docs/guides/routing/provider-selection"
title: "Provider Routing | Intelligent Multi-Provider Request Routing | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:51.759408+00:00"
---
[Models & Routing](../model-fallbacks/index.md)

# Provider Routing

Route requests to the best provider

OpenRouter routes requests to the best available providers for your model. By default, [requests are load balanced](#price-based-load-balancing-default-strategy) across the top providers to maximize uptime.

You can customize how your requests are routed using the `provider` object in the request body for [Chat Completions](../../../api-reference/chat-completion/index.md).

The `provider` object can contain the following fields:

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `order` | string[] | - | List of provider slugs to try in order (e.g. `["anthropic", "openai"]`). [Learn more](#ordering-specific-providers) |
| `allow_fallbacks` | boolean | `true` | Whether to allow backup providers when the primary is unavailable. [Learn more](#disabling-fallbacks) |
| `require_parameters` | boolean | `false` | Only use providers that support all parameters in your request. [Learn more](#requiring-providers-to-support-all-parameters-beta) |
| `data_collection` | ”allow” | “deny" | "allow” | Control whether to use providers that may store data. [Learn more](#requiring-providers-to-comply-with-data-policies) |
| `zdr` | boolean | - | Restrict routing to only ZDR (Zero Data Retention) endpoints. [Learn more](#zero-data-retention-enforcement) |
| `enforce_distillable_text` | boolean | - | Restrict routing to only models that allow text distillation. [Learn more](#distillable-text-enforcement) |
| `only` | string[] | - | List of provider slugs to allow for this request. [Learn more](#allowing-only-specific-providers) |
| `ignore` | string[] | - | List of provider slugs to skip for this request. [Learn more](#ignoring-providers) |
| `quantizations` | string[] | - | List of quantization levels to filter by (e.g. `["int4", "int8"]`). [Learn more](#quantization) |
| `sort` | string | object | - | Sort providers by price, throughput, or latency. Can be a string (e.g. `"price"`) or an object with `by` and `partition` fields. [Learn more](#provider-sorting) |
| `preferred_min_throughput` | number | object | - | Preferred minimum throughput (tokens/sec). Can be a number or an object with percentile cutoffs (p50, p75, p90, p99). [Learn more](#performance-thresholds) |
| `preferred_max_latency` | number | object | - | Preferred maximum latency (seconds). Can be a number or an object with percentile cutoffs (p50, p75, p90, p99). [Learn more](#performance-thresholds) |
| `max_price` | object | - | The maximum pricing you want to pay for this request. [Learn more](#maximum-price) |

##### EU data residency (Enterprise)

OpenRouter supports EU in-region routing for enterprise customers. When enabled, prompts and completions are processed entirely within the EU. Learn more in our [Privacy docs here](../../privacy/logging/index.md). To contact our enterprise team, [fill out this form](https://openrouter.ai/enterprise/form).

## Price-Based Load Balancing (Default Strategy)

For each model in your request, OpenRouter’s default behavior is to load balance requests across providers, prioritizing price.

If you are more sensitive to throughput than price, you can use the `sort` field to explicitly prioritize throughput.

##### 

When you send a request with `tools` or `tool_choice`, OpenRouter will only
route to providers that support tool use. Similarly, if you set a
`max_tokens`, then OpenRouter will only route to providers that support a
response of that length.

Here is OpenRouter’s default load balancing strategy:

1. Prioritize providers that have not seen significant outages in the last 30 seconds.
2. For the stable providers, look at the lowest-cost candidates and select one weighted by inverse square of the price (example below).
3. Use the remaining providers as fallbacks.

##### A Load Balancing Example

If Provider A costs $1 per million tokens, Provider B costs $2, and Provider C costs $3, and Provider B recently saw a few outages.

- Your request is routed to Provider A. Provider A is 9x more likely to be first routed to Provider A than Provider C because (1/32=1/9)(1 / 3^2 = 1/9)(1/32=1/9) (inverse square of the price).
- If Provider A fails, then Provider C will be tried next.
- If Provider C also fails, Provider B will be tried last.

If you have `sort` or `order` set in your provider preferences, load balancing will be disabled.

## Provider Sorting

As described above, OpenRouter load balances based on price, while taking uptime into account.

If you instead want to *explicitly* prioritize a particular provider attribute, you can include the `sort` field in the `provider` preferences. Load balancing will be disabled, and the router will try providers in order.

The three sort options are:

- `"price"`: prioritize lowest price
- `"throughput"`: prioritize highest throughput
- `"latency"`: prioritize lowest latency

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'meta-llama/llama-3.3-70b-instruct', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | sort: 'throughput', |
| 12 | }, |
| 13 | stream: false, |
| 14 | }); |
```

To *always* prioritize low prices, and not apply any load balancing, set `sort` to `"price"`.

To *always* prioritize low latency, and not apply any load balancing, set `sort` to `"latency"`.

## Nitro Shortcut

You can append `:nitro` to any model slug as a shortcut to sort by throughput. This is exactly equivalent to setting `provider.sort` to `"throughput"`.

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'meta-llama/llama-3.3-70b-instruct:nitro', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | stream: false, |
| 11 | }); |
```

## Floor Price Shortcut

You can append `:floor` to any model slug as a shortcut to sort by price. This is exactly equivalent to setting `provider.sort` to `"price"`.

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'meta-llama/llama-3.3-70b-instruct:floor', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | stream: false, |
| 11 | }); |
```

## Advanced Sorting with Partition

When using [model fallbacks](../../../features/model-routing/index.md), the `sort` field can be specified as an object with additional options to control how endpoints are sorted across multiple models.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `sort.by` | string | - | The sorting strategy: `"price"`, `"throughput"`, or `"latency"`. |
| `sort.partition` | string | `"model"` | How to group endpoints for sorting: `"model"` (default) or `"none"`. |

By default, when you specify multiple models (fallbacks), OpenRouter groups endpoints by model before sorting. This means the primary model’s endpoints are always tried first, regardless of their performance characteristics. Setting `partition` to `"none"` removes this grouping, allowing endpoints to be sorted globally across all models.

To explicitly use the default behavior, set `partition: "model"`. For more details on how model fallbacks work, see [Model Fallbacks](../model-fallbacks/index.md).

##### 

`preferred_max_latency` and `preferred_min_throughput` do *not* guarantee you will get a provider or model with this performance level. However, providers and models that hit your thresholds will be preferred. Specifying these preferences should therefore never prevent your request from being executed. This is different than `max_price`, which will prevent your request from running if the price is not available.

### Use Case 1: Route to the Highest Throughput or Lowest Latency Model

When you have multiple acceptable models and want to use whichever has the best performance right now, use `partition: "none"` with throughput or latency sorting. This is useful when you care more about speed than using a specific model.

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | models: [ |
| 9 | 'anthropic/claude-sonnet-4.5', |
| 10 | 'openai/gpt-5-mini', |
| 11 | 'google/gemini-3-flash-preview', |
| 12 | ], |
| 13 | messages: [{ role: 'user', content: 'Hello' }], |
| 14 | provider: { |
| 15 | sort: { |
| 16 | by: 'throughput', |
| 17 | partition: 'none', |
| 18 | }, |
| 19 | }, |
| 20 | stream: false, |
| 21 | }); |
```

In this example, OpenRouter will route to whichever endpoint across all three models currently has the highest throughput, rather than always trying Claude first.

## Performance Thresholds

You can set minimum throughput or maximum latency thresholds to filter endpoints. Endpoints that don’t meet these thresholds are deprioritized (moved to the end of the list) rather than excluded entirely.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `preferred_min_throughput` | number | object | - | Preferred minimum throughput in tokens per second. Can be a number (applies to p50) or an object with percentile cutoffs. |
| `preferred_max_latency` | number | object | - | Preferred maximum latency in seconds. Can be a number (applies to p50) or an object with percentile cutoffs. |

### How Percentiles Work

OpenRouter tracks latency and throughput metrics for each model and provider using percentile statistics calculated over a rolling 5-minute window. The available percentiles are:

- **p50** (median): 50% of requests perform better than this value
- **p75**: 75% of requests perform better than this value
- **p90**: 90% of requests perform better than this value
- **p99**: 99% of requests perform better than this value

Higher percentiles (like p90 or p99) give you more confidence about worst-case performance, while lower percentiles (like p50) reflect typical performance. For example, if a model and provider has a p90 latency of 2 seconds, that means 90% of requests complete in under 2 seconds.

When you specify multiple percentile cutoffs, all specified cutoffs must be met for a model and provider to be in the preferred group. This allows you to set both typical and worst-case performance requirements.

### When to Use Percentile Preferences

Percentile-based routing is useful when you need predictable performance characteristics:

- **Real-time applications**: Use p90 or p99 latency thresholds to ensure consistent response times for user-facing features
- **Batch processing**: Use p50 throughput thresholds when you care more about average performance than worst-case scenarios
- **SLA compliance**: Use multiple percentile cutoffs to ensure providers meet your service level agreements across different performance tiers
- **Cost optimization**: Combine with `sort: "price"` to get the cheapest provider that still meets your performance requirements

### Use Case 2: Find the Cheapest Model Meeting Performance Requirements

Combine `partition: "none"` with performance thresholds to find the cheapest option across multiple models that meets your performance requirements. This is useful when you have a performance floor but want to minimize costs.

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | models: [ |
| 9 | 'anthropic/claude-sonnet-4.5', |
| 10 | 'openai/gpt-5-mini', |
| 11 | 'google/gemini-3-flash-preview', |
| 12 | ], |
| 13 | messages: [{ role: 'user', content: 'Hello' }], |
| 14 | provider: { |
| 15 | sort: { |
| 16 | by: 'price', |
| 17 | partition: 'none', |
| 18 | }, |
| 19 | preferredMinThroughput: { |
| 20 | p90: 50, // Prefer providers with >50 tokens/sec for 90% of requests in last 5 minutes |
| 21 | }, |
| 22 | }, |
| 23 | stream: false, |
| 24 | }); |
```

In this example, OpenRouter will find the cheapest model and provider across all three models that has at least 50 tokens/second throughput at the p90 level (meaning 90% of requests achieve this throughput or better). Models and providers below this threshold are still available as fallbacks if all preferred options fail.

You can also use `preferred_max_latency` to set a maximum acceptable latency:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | models: [ |
| 9 | 'anthropic/claude-sonnet-4.5', |
| 10 | 'openai/gpt-5-mini', |
| 11 | ], |
| 12 | messages: [{ role: 'user', content: 'Hello' }], |
| 13 | provider: { |
| 14 | sort: { |
| 15 | by: 'price', |
| 16 | partition: 'none', |
| 17 | }, |
| 18 | preferredMaxLatency: { |
| 19 | p90: 3, // Prefer providers with <3 second latency for 90% of requests in last 5 minutes |
| 20 | }, |
| 21 | }, |
| 22 | stream: false, |
| 23 | }); |
```

### Example: Using Multiple Percentile Cutoffs

You can specify multiple percentile cutoffs to set both typical and worst-case performance requirements. All specified cutoffs must be met for a model and provider to be in the preferred group.

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'deepseek/deepseek-v3.2', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | preferredMaxLatency: { |
| 12 | p50: 1, // Prefer providers with <1 second latency for 50% of requests in last 5 minutes |
| 13 | p90: 3, // Prefer providers with <3 second latency for 90% of requests in last 5 minutes |
| 14 | p99: 5, // Prefer providers with <5 second latency for 99% of requests in last 5 minutes |
| 15 | }, |
| 16 | preferredMinThroughput: { |
| 17 | p50: 100, // Prefer providers with >100 tokens/sec for 50% of requests in last 5 minutes |
| 18 | p90: 50, // Prefer providers with >50 tokens/sec for 90% of requests in last 5 minutes |
| 19 | }, |
| 20 | }, |
| 21 | stream: false, |
| 22 | }); |
```

### Use Case 3: Maximize BYOK Usage Across Models

If you use [Bring Your Own Key (BYOK)](../../overview/auth/byok/index.md) and want to maximize usage of your own API keys, `partition: "none"` can help. When your primary model doesn’t have a BYOK provider available, OpenRouter can route to a fallback model that does support BYOK.

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | models: [ |
| 9 | 'anthropic/claude-sonnet-4.5', |
| 10 | 'openai/gpt-5-mini', |
| 11 | 'google/gemini-3-flash-preview', |
| 12 | ], |
| 13 | messages: [{ role: 'user', content: 'Hello' }], |
| 14 | provider: { |
| 15 | sort: { |
| 16 | by: 'price', |
| 17 | partition: 'none', |
| 18 | }, |
| 19 | }, |
| 20 | stream: false, |
| 21 | }); |
```

In this example, if you have a BYOK key configured for OpenAI but not for Anthropic, OpenRouter can route to the GPT-4o endpoint using your own key even though Claude is listed first. Without `partition: "none"`, the router would always try Claude’s endpoints first before falling back to GPT-4o.

##### 

BYOK endpoints are automatically prioritized when you have API keys configured for a provider. The `partition: "none"` setting allows this prioritization to work across model boundaries.

## Ordering Specific Providers

You can set the providers that OpenRouter will prioritize for your request using the `order` field.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `order` | string[] | - | List of provider slugs to try in order (e.g. `["anthropic", "openai"]`). |

The router will prioritize providers in this list, and in this order, for the model you’re using. If you don’t set this field, the router will [load balance](#price-based-load-balancing-default-strategy) across the top providers to maximize uptime.

##### 

You can use the copy button next to provider names on model pages to get the exact provider slug,
including any variants like “/turbo”. See [Targeting Specific Provider Endpoints](#targeting-specific-provider-endpoints) for details.

OpenRouter will try them one at a time and proceed to other providers if none are operational. If you don’t want to allow any other providers, you should [disable fallbacks](#disabling-fallbacks) as well.

### Example: Specifying providers with fallbacks

This example skips over OpenAI (which doesn’t host Mixtral), tries Together, and then falls back to the normal list of providers on OpenRouter:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'mistralai/mixtral-8x7b-instruct', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | order: ['openai', 'together'], |
| 12 | }, |
| 13 | stream: false, |
| 14 | }); |
```

### Example: Specifying providers with fallbacks disabled

Here’s an example with `allow_fallbacks` set to `false` that skips over OpenAI (which doesn’t host Mixtral), tries Together, and then fails if Together fails:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'mistralai/mixtral-8x7b-instruct', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | order: ['openai', 'together'], |
| 12 | allowFallbacks: false, |
| 13 | }, |
| 14 | stream: false, |
| 15 | }); |
```

## Targeting Specific Provider Endpoints

Each provider on OpenRouter may host multiple endpoints for the same model, such as a default endpoint and a specialized “turbo” endpoint, or region-specific endpoints like `google-vertex/us-east5`. To target a specific endpoint, you can use the copy button next to the provider name on the model detail page to obtain the exact provider slug.

### Base Slug Matching

When you use a base provider slug (e.g. `"google-vertex"`) in any provider routing field (`order`, `only`, or `ignore`), it matches **all** endpoints for that provider, including any variants or regions. For example, `"google-vertex"` matches `google-vertex`, `google-vertex/us-east5`, `google-vertex/us-central1`, and so on.

To target a **specific** variant or region, use the full slug including the suffix (e.g. `"google-vertex/us-east5"` or `"deepinfra/turbo"`).

| Slug in request | What it matches |
| --- | --- |
| `"google-vertex"` | All Google Vertex endpoints (every region) |
| `"google-vertex/us-east5"` | Only the `us-east5` region endpoint |
| `"deepinfra"` | All DeepInfra endpoints (default + turbo) |
| `"deepinfra/turbo"` | Only the DeepInfra turbo endpoint |

### Example: Targeting a specific endpoint variant

For example, DeepInfra offers DeepSeek R1 through multiple endpoints:

- Default endpoint with slug `deepinfra`
- Turbo endpoint with slug `deepinfra/turbo`

By copying the exact provider slug and using it in your request’s `order` array, you can ensure your request is routed to the specific endpoint you want:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'deepseek/deepseek-r1', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | order: ['deepinfra/turbo'], |
| 12 | allowFallbacks: false, |
| 13 | }, |
| 14 | stream: false, |
| 15 | }); |
```

This approach is especially useful when you want to consistently use a specific variant of a model from a particular provider.

##### 

To route to **all** endpoints of a provider (across all regions and variants), just use the base slug without a suffix. For example, `"google-vertex"` will route across all Vertex AI regions.

## Requiring Providers to Support All Parameters

You can restrict requests only to providers that support all parameters in your request using the `require_parameters` field.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `require_parameters` | boolean | `false` | Only use providers that support all parameters in your request. |

With the default routing strategy, providers that don’t support all the [LLM parameters](../../../api-reference/parameters/index.md) specified in your request can still receive the request, but will ignore unknown parameters. When you set `require_parameters` to `true`, the request won’t even be routed to that provider.

### Example: Excluding providers that don’t support JSON formatting

For example, to only use providers that support JSON formatting:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | messages: [{ role: 'user', content: 'Hello' }], |
| 9 | provider: { |
| 10 | requireParameters: true, |
| 11 | }, |
| 12 | responseFormat: { type: 'json_object' }, |
| 13 | stream: false, |
| 14 | }); |
```

## Requiring Providers to Comply with Data Policies

You can restrict requests only to providers that comply with your data policies using the `data_collection` field.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `data_collection` | ”allow” | “deny" | "allow” | Control whether to use providers that may store data. |

- `allow`: (default) allow providers which store user data non-transiently and may train on it
- `deny`: use only providers which do not collect user data

Some model providers may log prompts, so we display them with a **Data Policy** tag on model pages. This is not a definitive source of third party data policies, but represents our best knowledge.

##### Account-Wide Data Policy Filtering

This is also available as an account-wide setting in [your privacy
settings](https://openrouter.ai/settings/privacy). You can disable third party
model providers that store inputs for training.

### Example: Excluding providers that don’t comply with data policies

To exclude providers that don’t comply with your data policies, set `data_collection` to `deny`:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | messages: [{ role: 'user', content: 'Hello' }], |
| 9 | provider: { |
| 10 | dataCollection: 'deny', // or "allow" |
| 11 | }, |
| 12 | stream: false, |
| 13 | }); |
```

## Zero Data Retention Enforcement

You can enforce Zero Data Retention (ZDR) on a per-request basis using the `zdr` parameter, ensuring your request only routes to endpoints that do not retain prompts.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `zdr` | boolean | - | Restrict routing to only ZDR (Zero Data Retention) endpoints. |

When `zdr` is set to `true`, the request will only be routed to endpoints that have a Zero Data Retention policy. When `zdr` is `false` or not provided, it has no effect on routing.

##### Account-Wide ZDR Setting

This is also available as an account-wide setting in [your privacy
settings](https://openrouter.ai/settings/privacy). The per-request `zdr` parameter
operates as an “OR” with your account-wide ZDR setting - if either is enabled, ZDR enforcement will be applied. The request-level parameter can only ensure ZDR is enabled, not override account-wide enforcement.

### Example: Enforcing ZDR for a specific request

To ensure a request only uses ZDR endpoints, set `zdr` to `true`:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'gpt-4', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | zdr: true, |
| 12 | }, |
| 13 | stream: false, |
| 14 | }); |
```

This is useful for customers who don’t want to globally enforce ZDR but need to ensure specific requests only route to ZDR endpoints.

## Distillable Text Enforcement

You can enforce distillable text filtering on a per-request basis using the `enforce_distillable_text` parameter, ensuring your request only routes to models where the author has allowed text distillation.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `enforce_distillable_text` | boolean | - | Restrict routing to only models that allow text distillation. |

When `enforce_distillable_text` is set to `true`, the request will only be routed to models where the author has explicitly enabled text distillation. When `enforce_distillable_text` is `false` or not provided, it has no effect on routing.

This parameter is useful for applications that need to ensure their requests only use models that allow text distillation for training purposes, such as when building datasets for model fine-tuning or distillation workflows.

### Example: Enforcing distillable text for a specific request

To ensure a request only uses models that allow text distillation, set `enforce_distillable_text` to `true`:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'meta-llama/llama-3.3-70b-instruct', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | enforceDistillableText: true, |
| 12 | }, |
| 13 | stream: false, |
| 14 | }); |
```

## Disabling Fallbacks

To guarantee that your request is only served by the top (lowest-cost) provider, you can disable fallbacks.

This is combined with the `order` field from [Ordering Specific Providers](#ordering-specific-providers) to restrict the providers that OpenRouter will prioritize to just your chosen list.

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | messages: [{ role: 'user', content: 'Hello' }], |
| 9 | provider: { |
| 10 | allowFallbacks: false, |
| 11 | }, |
| 12 | stream: false, |
| 13 | }); |
```

## Allowing Only Specific Providers

You can allow only specific providers for a request by setting the `only` field in the `provider` object.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `only` | string[] | - | List of provider slugs to allow for this request. |

##### 

Only allowing some providers may significantly reduce fallback options and
limit request recovery.

##### Account-Wide Allowed Providers

You can allow providers for all account requests in your [privacy settings](https://openrouter.ai/settings/privacy). This configuration applies to all API requests and chatroom messages.

Note that when you allow providers for a specific request, the list of allowed providers is merged with your account-wide allowed providers.

### Example: Allowing Azure for a request calling GPT-4 Omni

Here’s an example that will only use Azure for a request calling GPT-4 Omni:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'openai/gpt-5-mini', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | only: ['azure'], |
| 12 | }, |
| 13 | stream: false, |
| 14 | }); |
```

## Ignoring Providers

You can ignore providers for a request by setting the `ignore` field in the `provider` object.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `ignore` | string[] | - | List of provider slugs to skip for this request. |

##### 

Ignoring multiple providers may significantly reduce fallback options and
limit request recovery.

##### Account-Wide Ignored Providers

You can ignore providers for all account requests in your [privacy settings](https://openrouter.ai/settings/privacy). This configuration applies to all API requests and chatroom messages.

Note that when you ignore providers for a specific request, the list of ignored providers is merged with your account-wide ignored providers.

### Example: Ignoring DeepInfra for a request calling Llama 3.3 70b

Here’s an example that will ignore DeepInfra for a request calling Llama 3.3 70b:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'meta-llama/llama-3.3-70b-instruct', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | ignore: ['deepinfra'], |
| 12 | }, |
| 13 | stream: false, |
| 14 | }); |
```

## Quantization

Quantization reduces model size and computational requirements while aiming to preserve performance. Most LLMs today use FP16 or BF16 for training and inference, cutting memory requirements in half compared to FP32. Some optimizations use FP8 or quantization to reduce size further (e.g., INT8, INT4).

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `quantizations` | string[] | - | List of quantization levels to filter by (e.g. `["int4", "int8"]`). [Learn more](#quantization) |

##### 

Quantized models may exhibit degraded performance for certain prompts,
depending on the method used.

Providers can support various quantization levels for open-weight models.

### Quantization Levels

By default, requests are load-balanced across all available providers, ordered by price. To filter providers by quantization level, specify the `quantizations` field in the `provider` parameter with the following values:

- `int4`: Integer (4 bit)
- `int8`: Integer (8 bit)
- `fp4`: Floating point (4 bit)
- `fp6`: Floating point (6 bit)
- `fp8`: Floating point (8 bit)
- `fp16`: Floating point (16 bit)
- `bf16`: Brain floating point (16 bit)
- `fp32`: Floating point (32 bit)
- `unknown`: Unknown

### Example: Requesting FP8 Quantization

Here’s an example that will only use providers that support FP8 quantization:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send({ |
| 8 | model: 'meta-llama/llama-3.1-8b-instruct', |
| 9 | messages: [{ role: 'user', content: 'Hello' }], |
| 10 | provider: { |
| 11 | quantizations: ['fp8'], |
| 12 | }, |
| 13 | stream: false, |
| 14 | }); |
```

### Max Price

To filter providers by price, specify the `max_price` field in the `provider` parameter with a JSON object specifying the highest provider pricing you will accept.

For example, the value `{"prompt": 1, "completion": 2}` will route to any provider with a price of `<= $1/m` prompt tokens, and `<= $2/m` completion tokens or less.

Some providers support per request pricing, in which case you can use the `request` attribute of max\_price. Lastly, `image` is also available, which specifies the max price per image you will accept.

Practically, this field is often combined with a provider `sort` to express, for example, “Use the provider with the highest throughput, as long as it doesn’t cost more than `$x/m` tokens.”

## Provider-Specific Headers

Some providers support beta features that can be enabled through special headers. OpenRouter allows you to pass through certain provider-specific beta headers when making requests.

### Anthropic Beta Features

When using Anthropic models (Claude), you can request specific beta features by including the `x-anthropic-beta` header in your request. OpenRouter will pass through supported beta features to Anthropic.

#### Supported Beta Features

| Feature | Header Value | Description |
| --- | --- | --- |
| Fine-Grained Tool Streaming | `fine-grained-tool-streaming-2025-05-14` | Enables more granular streaming events during tool calls, providing real-time updates as tool arguments are being generated |
| Interleaved Thinking | `interleaved-thinking-2025-05-14` | Allows Claude’s thinking/reasoning to be interleaved with regular output, rather than appearing as a single block |
| Structured Outputs | `structured-outputs-2025-11-13` | Enables the strict tool use feature for supported Claude models, validating tool parameters against your schema to ensure correctly-typed arguments |

##### 

OpenRouter manages some Anthropic beta features automatically:

- **Prompt caching and extended context** are enabled based on model capabilities
- **Structured outputs for JSON schema response format** (`response_format.type: "json_schema"`) - the header is automatically applied

For **strict tool use** (`strict: true` on tools), you must explicitly pass the `structured-outputs-2025-11-13` header. Without this header, OpenRouter will strip the `strict` field and route normally.

#### Example: Enabling Fine-Grained Tool Streaming

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send( |
| 8 | { |
| 9 | model: 'anthropic/claude-sonnet-4.5', |
| 10 | messages: [{ role: 'user', content: 'What is the weather in Tokyo?' }], |
| 11 | tools: [ |
| 12 | { |
| 13 | type: 'function', |
| 14 | function: { |
| 15 | name: 'get_weather', |
| 16 | description: 'Get the current weather for a location', |
| 17 | parameters: { |
| 18 | type: 'object', |
| 19 | properties: { |
| 20 | location: { type: 'string' }, |
| 21 | }, |
| 22 | required: ['location'], |
| 23 | }, |
| 24 | }, |
| 25 | }, |
| 26 | ], |
| 27 | stream: true, |
| 28 | }, |
| 29 | { |
| 30 | headers: { |
| 31 | 'x-anthropic-beta': 'fine-grained-tool-streaming-2025-05-14', |
| 32 | }, |
| 33 | }, |
| 34 | ); |
```

#### Example: Enabling Interleaved Thinking

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const openRouter = new OpenRouter({ |
| 4 | apiKey: '<OPENROUTER_API_KEY>', |
| 5 | }); |
| 6 |  |
| 7 | const completion = await openRouter.chat.send( |
| 8 | { |
| 9 | model: 'anthropic/claude-sonnet-4.5', |
| 10 | messages: [{ role: 'user', content: 'Solve this step by step: What is 15% of 240?' }], |
| 11 | stream: true, |
| 12 | }, |
| 13 | { |
| 14 | headers: { |
| 15 | 'x-anthropic-beta': 'interleaved-thinking-2025-05-14', |
| 16 | }, |
| 17 | }, |
| 18 | ); |
```

#### Combining Multiple Beta Features

You can enable multiple beta features by separating them with commas:

```
|  |  |
| --- | --- |
| $ | x-anthropic-beta: fine-grained-tool-streaming-2025-05-14,interleaved-thinking-2025-05-14 |
```

##### 

Beta features are experimental and may change or be deprecated by Anthropic. Check [Anthropic’s documentation](https://docs.anthropic.com/en/api/beta-features) for the latest information on available beta features.

## Terms of Service

You can view the terms of service for each provider below. You may not violate the terms of service or policies of third-party providers that power the models on OpenRouter.
