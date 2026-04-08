---
source_url: "https://openrouter.ai/docs/guides/best-practices/uptime-optimization"
title: "Uptime Optimization | Maximize AI Model Availability | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:31.664767+00:00"
---
[Best Practices](../latency-and-performance/index.md)

# Uptime Optimization

OpenRouter tracks provider availability

OpenRouter continuously monitors the health and availability of AI providers to ensure maximum uptime for your applications. We track response times, error rates, and availability across all providers in real-time, and route based on this feedback.

## How It Works

OpenRouter tracks response times, error rates, and availability across all providers in real-time. This data helps us make intelligent routing decisions and provides transparency about service reliability.

## Uptime Example: Claude 4 Sonnet

## Uptime Example: Llama 3.3 70B Instruct

## Customizing Provider Selection

While our smart routing helps maintain high availability, you can also customize provider selection using request parameters. This gives you control over which providers handle your requests while still benefiting from automatic fallback when needed.

Learn more about customizing provider selection in our [Provider Routing documentation](../../../features/provider-routing/index.md).
