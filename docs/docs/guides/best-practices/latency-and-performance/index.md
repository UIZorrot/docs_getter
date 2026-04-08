---
source_url: "https://openrouter.ai/docs/guides/best-practices/latency-and-performance"
title: "Latency and Performance | Minimizing Gateway Latency | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:31.701431+00:00"
---
[Best Practices](index.md)

# Latency and Performance

Understanding OpenRouter's performance characteristics

OpenRouter is designed with performance as a top priority. OpenRouter is heavily optimized to add as little latency as possible to your requests.

## Minimal Overhead

OpenRouter is designed to add minimal latency to your requests. This is achieved through:

- Edge computing using Cloudflare Workers to stay as close as possible to your application
- Efficient caching of user and API key data at the edge
- Optimized routing logic that minimizes processing time

## Performance Considerations

### Cache Warming

When OpenRouter’s edge caches are cold (typically during the first 1-2 minutes of operation in a new region), you may experience slightly higher latency as the caches warm up. This normalizes once the caches are populated.

### Credit Balance Checks

To maintain accurate billing and prevent overages, OpenRouter performs additional database checks when:

- A user’s credit balance is low (single digit dollars)
- An API key is approaching its configured credit limit

OpenRouter expires caches more aggressively under these conditions to ensure proper billing, which increases latency until additional credits are added.

### Model Fallback

When using [model routing](../../../routing/auto-model-selection/index.md) or [provider routing](../../../features/provider-routing/index.md), if the primary model or provider fails, OpenRouter will automatically try the next option. A failed initial completion unsurprisingly adds latency to the specific request. OpenRouter tracks provider failures, and will attempt to intelligently route around unavailable providers so that this latency is not incurred on every request.

## Best Practices

To achieve optimal performance with OpenRouter:

1. **Maintain Healthy Credit Balance**

   - Set up auto-topup with a higher threshold and amount
   - This helps avoid forced credit checks and reduces the risk of hitting zero balance
   - Recommended minimum balance: $10-20 to ensure smooth operation
2. **Use Provider Preferences**

   - If you have specific latency requirements (whether time to first token, or time to last), there are [provider routing](../../../features/provider-routing/index.md) features to help you achieve your performance and cost goals.
