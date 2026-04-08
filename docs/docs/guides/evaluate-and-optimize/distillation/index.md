---
source_url: "https://openrouter.ai/docs/guides/evaluate-and-optimize/distillation"
title: "Distillation | Compliance with Provider and Model Creator Policies | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:35.519904+00:00"
---
[Guides](../../administration/activity-export/index.md)[Evaluate & Optimize](index.md)

# Distillation

Ensure compliance with provider and model creator policies for distillation

Model distillation is the process of training a smaller, more efficient model using outputs from a larger model. While this technique is powerful for creating specialized models, it’s important to respect the terms of service set by model providers and creators.

Some model providers and creators explicitly prohibit using their model outputs to train other models, while others allow it. OpenRouter makes it easy to filter for models that permit distillation, helping you stay compliant with these policies.

## Why Distillation Compliance Matters

When you use model outputs to train or fine-tune other models, you need to ensure you have permission to do so. Using outputs from models that prohibit distillation could violate terms of service agreements and potentially expose you to legal liability.

OpenRouter tracks which models allow their outputs to be used for training purposes through the `is_trainable_text` property. Models where the author has explicitly allowed text distillation are marked as distillable.

##### 

OpenRouter provides distillation information on a best-effort basis. You should always verify the specific license terms for your use case, as licensing requirements may vary depending on how you intend to use the model outputs.

## Finding Distillable Models on the Model Page

The easiest way to find models that allow distillation is to use the **Distillable** filter on the [Models page](https://openrouter.ai/models).

1. Navigate to the [Models page with the distillable filter enabled](https://openrouter.ai/models)
2. The **Distillable** filter in the filter panel will be set to **Yes**, showing only models that allow distillation

This filter shows you all models where the author has permitted their outputs to be used for training purposes, making it easy to build compliant distillation workflows.

## Using the Routing Parameter

For programmatic control, you can use the `enforce_distillable_text` parameter in your API requests. When set to `true`, OpenRouter will only route your request to models that allow text distillation.

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `enforce_distillable_text` | boolean | - | Restrict routing to only models that allow text distillation. |

When `enforce_distillable_text` is set to `true`, the request will only be routed to models where the author has explicitly enabled text distillation. If no distillable models are available for your request, you’ll receive an error.

### Example: Enforcing Distillable Models

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
| 8 | model: 'meta-llama/llama-3.1-70b-instruct', |
| 9 | messages: [{ role: 'user', content: 'Explain quantum computing' }], |
| 10 | provider: { |
| 11 | enforceDistillableText: true, |
| 12 | }, |
| 13 | stream: false, |
| 14 | }); |
```

## Use Cases

The distillable filter is particularly useful for:

- **Building training datasets**: When collecting model outputs to train or fine-tune your own models, ensure you only use outputs from models that permit this use.
- **Distillation pipelines**: When creating smaller, specialized models from larger teacher models, filter for models that allow their outputs to be used for training.
- **Compliance workflows**: Organizations with strict compliance requirements can enforce distillation policies programmatically across all API requests.

## Related Documentation

- [Provider Routing](../../../features/provider-routing/index.md) - Learn more about the `enforce_distillable_text` parameter and other provider routing options
- [Models](../../../overview/models/index.md) - Browse all available models and their capabilities
