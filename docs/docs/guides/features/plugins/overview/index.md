---
source_url: "https://openrouter.ai/docs/guides/features/plugins/overview"
title: "Plugins | Extend AI Model Capabilities | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:51.917101+00:00"
---
[Features](../../presets/index.md)[Plugins](index.md)

# Plugins

Extend model capabilities with OpenRouter plugins

OpenRouter plugins extend the capabilities of any model by injecting or mutating a request or response to add functionality like PDF processing, automatic JSON repair, and context compression. Unlike [server tools](../../server-tools/index.md) (which the model can call 0-N times), plugins always run once when enabled. Plugins can be enabled per-request via the API or configured as defaults for all your API requests through the [Plugins settings page](https://openrouter.ai/settings/plugins).

## Available Plugins

OpenRouter currently supports the following plugins:

| Plugin | Description | Docs |
| --- | --- | --- |
| **Web Search** (deprecated) | Augment LLM responses with real-time web search results. Use the [`openrouter:web_search` server tool](../../server-tools/web-search/index.md) instead. | [Web Search](../web-search/index.md) |
| **PDF Inputs** | Parse and extract content from uploaded PDF files | [PDF Inputs](../../../overview/multimodal/pdfs/index.md) |
| **Response Healing** | Automatically fix malformed JSON responses from LLMs | [Response Healing](../response-healing/index.md) |
| **Context Compression** | Compress prompts that exceed a model’s context window using middle-out truncation | [Message Transforms](../../message-transforms/index.md) |

## Enabling Plugins via API

Plugins are enabled by adding a `plugins` array to your chat completions request. Each plugin is identified by its `id` and can include optional configuration parameters.

```
|  |  |
| --- | --- |
| 1 | const response = await fetch('https://openrouter.ai/api/v1/chat/completions', { |
| 2 | method: 'POST', |
| 3 | headers: { |
| 4 | Authorization: 'Bearer {{API_KEY_REF}}', |
| 5 | 'Content-Type': 'application/json', |
| 6 | }, |
| 7 | body: JSON.stringify({ |
| 8 | model: '{{MODEL}}', |
| 9 | messages: [ |
| 10 | { |
| 11 | role: 'user', |
| 12 | content: 'What are the latest developments in AI?' |
| 13 | } |
| 14 | ], |
| 15 | plugins: [ |
| 16 | { id: 'web' } |
| 17 | ] |
| 18 | }), |
| 19 | }); |
| 20 |  |
| 21 | const data = await response.json(); |
| 22 | console.log(data.choices[0].message.content); |
```

## Using Multiple Plugins

You can enable multiple plugins in a single request:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2", |
| 3 | "messages": [...], |
| 4 | "plugins": [ |
| 5 | { "id": "web", "max_results": 3 }, |
| 6 | { "id": "response-healing" } |
| 7 | ], |
| 8 | "response_format": { |
| 9 | "type": "json_schema", |
| 10 | "json_schema": { ... } |
| 11 | } |
| 12 | } |
```

## Default Plugin Settings

Organization admins and individual users can configure default plugin settings that apply to all API requests. This is useful for:

- Enabling plugins like web search or response healing by default across all requests
- Setting consistent plugin configurations without modifying application code
- Enforcing plugin settings that cannot be overridden by individual requests

To configure default plugin settings:

1. Navigate to [Settings > Plugins](https://openrouter.ai/settings/plugins)
2. Toggle plugins on/off to enable them by default
3. Click the configure button to customize plugin settings
4. Optionally enable “Prevent overrides” to enforce settings across all requests

##### 

In organizations, the Plugins settings page is only accessible to admins.

##### 

When “Prevent overrides” is enabled for a plugin, individual API requests cannot disable or modify that plugin’s configuration. This is useful for enforcing organization-wide policies.

### Plugin precedence

Plugin settings are applied in the following order of precedence:

1. **Request-level settings**: Plugin configurations in the `plugins` array of individual requests
2. **Account defaults**: Settings configured in the Plugins settings page

If a plugin is enabled in your account defaults but not specified in a request, the default configuration will be applied. If you specify a plugin in your request, those settings will override the defaults.

If you want the account setting to take precedence, toggle on “Prevent overrides” in the config for the plugin. It will then be impossible for generations to override the config.

### Disabling a default plugin

If a plugin is enabled by default in your account settings, you can disable it for a specific request by passing `"enabled": false` in the plugins array:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2", |
| 3 | "messages": [...], |
| 4 | "plugins": [ |
| 5 | { "id": "web", "enabled": false } |
| 6 | ] |
| 7 | } |
```

This will turn off the web search plugin for that particular request, even if it’s enabled in your account defaults.

## Model Variants as Plugin Shortcuts

##### Deprecated

The `:online` variant and the web search plugin are deprecated. Use the [`openrouter:web_search` server tool](../../server-tools/web-search/index.md) instead.

Some plugins have convenient model variant shortcuts. For example, appending `:online` to any model ID enables web search:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2:online" |
| 3 | } |
```

This is equivalent to:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-5.2", |
| 3 | "plugins": [{ "id": "web" }] |
| 4 | } |
```

See [Model Variants](../../../routing/model-variants/index.md) for more information about available shortcuts.
