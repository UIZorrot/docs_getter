---
source_url: "https://openrouter.ai/docs/guides/features/plugins/response-healing"
title: "Response Healing | Validate and Repair AI Model Responses | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:38.295423+00:00"
---
[Features](../../presets/index.md)[Plugins](../overview/index.md)

# Response Healing

Automatically fix malformed JSON responses

The Response Healing plugin automatically validates and repairs malformed JSON responses from AI models. When models return imperfect formatting – missing brackets, trailing commas, markdown wrappers, or mixed text – this plugin attempts to repair the response so you receive valid, parseable JSON.

## Overview

Response Healing provides:

- **Automatic JSON repair**: Fixes missing brackets, commas, quotes, and other syntax errors
- **Markdown extraction**: Extracts JSON from markdown code blocks

## How It Works

The plugin activates for non-streaming requests when you use `response_format` with either `type: "json_schema"` or `type: "json_object"`, and include the response-healing plugin in your `plugins` array. See the [Complete Example](#complete-example) below for a full implementation.

## What Gets Fixed

The Response Healing plugin handles common issues in LLM responses:

### JSON Syntax Errors

**Input:** Missing closing bracket

```
|  |
| --- |
| {"name": "Alice", "age": 30 |
```

**Output:** Fixed

```
|  |  |
| --- | --- |
| 1 | {"name": "Alice", "age": 30} |
```

### Markdown Code Blocks

**Input:** Wrapped in markdown

```
|  |
| --- |
| ```json |
| {"name": "Bob"} |
| ``` |
```

**Output:** Extracted

```
|  |  |
| --- | --- |
| 1 | {"name": "Bob"} |
```

### Mixed Text and JSON

**Input:** Text before JSON

```
|  |
| --- |
| Here's the data you requested: |
| {"name": "Charlie", "age": 25} |
```

**Output:** Extracted

```
|  |  |
| --- | --- |
| 1 | {"name": "Charlie", "age": 25} |
```

### Trailing Commas

**Input:** Invalid trailing comma

```
|  |
| --- |
| {"name": "David", "age": 35,} |
```

**Output:** Fixed

```
|  |  |
| --- | --- |
| 1 | {"name": "David", "age": 35} |
```

### Unquoted Keys

**Input:** JavaScript-style

```
|  |
| --- |
| {name: "Eve", age: 40} |
```

**Output:** Fixed

```
|  |  |
| --- | --- |
| 1 | {"name": "Eve", "age": 40} |
```

## Complete Example

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
| 12 | content: 'Generate a product listing with name, price, and description' |
| 13 | } |
| 14 | ], |
| 15 | response_format: { |
| 16 | type: 'json_schema', |
| 17 | json_schema: { |
| 18 | name: 'Product', |
| 19 | schema: { |
| 20 | type: 'object', |
| 21 | properties: { |
| 22 | name: { |
| 23 | type: 'string', |
| 24 | description: 'Product name' |
| 25 | }, |
| 26 | price: { |
| 27 | type: 'number', |
| 28 | description: 'Price in USD' |
| 29 | }, |
| 30 | description: { |
| 31 | type: 'string', |
| 32 | description: 'Product description' |
| 33 | } |
| 34 | }, |
| 35 | required: ['name', 'price'] |
| 36 | } |
| 37 | } |
| 38 | }, |
| 39 | plugins: [ |
| 40 | { id: 'response-healing' } |
| 41 | ] |
| 42 | }), |
| 43 | }); |
| 44 |  |
| 45 | const data = await response.json(); |
| 46 | const product = JSON.parse(data.choices[0].message.content); |
| 47 | // The plugin attempts to repair malformed JSON syntax |
| 48 | console.log(product.name, product.price); |
```

## Limitations

##### Non-Streaming Requests Only

Response Healing only applies to non-streaming requests.

##### Will not repair all JSON

Some malformed JSON responses may still be unrepairable. In particular, if the response is truncated by `max_tokens`, the plugin will not be able to repair it.
