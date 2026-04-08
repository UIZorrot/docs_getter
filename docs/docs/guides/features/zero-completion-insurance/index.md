---
source_url: "https://openrouter.ai/docs/guides/features/zero-completion-insurance"
title: "Zero Completion Insurance | No Charge for Zero Token Responses | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:39.212732+00:00"
---
[Features](../presets/index.md)

# Zero Completion Insurance

OpenRouter will not charge you for zero token responses

OpenRouter provides zero completion insurance to protect users from being charged for failed or empty responses. When a response contains no output tokens and either has a blank finish reason or an error, you will not be charged for the request, even if the underlying provider charges for prompt processing.

##### 

Zero completion insurance is automatically enabled for all accounts and requires no configuration.

## How It Works

Zero completion insurance automatically applies to all requests across all models and providers. When a response meets either of these conditions, no credits will be deducted from your account:

- The response has zero completion tokens AND a blank/null finish reason
- The response has an error finish reason

## Viewing Protected Requests

On your activity page, requests that were protected by zero completion insurance will show zero credits deducted. This applies even in cases where OpenRouter may have been charged by the provider for prompt processing.
