---
source_url: "https://openrouter.ai/docs/sdks/dev-tools/devtools"
title: "DevTools | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:43.876256+00:00"
---
[DevTools](index.md)

# DevTools

SDK Development Tools for telemetry capture and visualization

##### 

The DevTools SDK and CLI are currently in pre-release status. DevTools is designed for development use only and should never be deployed in production environments.

The OpenRouter DevTools provide a comprehensive solution for SDK telemetry capture and visualization during development. Monitor your AI application’s requests, responses, token usage, and errors in real-time with a beautiful web interface.

## Why use DevTools?

Building with AI SDKs requires visibility into what’s happening under the hood. The OpenRouter DevTools give you complete insight into your SDK operations without adding complexity or impacting performance.

**Two main components:**

1. **SDK Telemetry Hooks** - Automatically capture all SDK operations in development
2. **DevTools Viewer** - Beautiful web UI for visualizing captured telemetry data

## Key Features

### SDK DevTools Viewer

Launch a web-based interface to visualize your SDK telemetry:

- **Real-time run tracking** - View all SDK operations (chat, embeddings, etc.) as they happen
- **Detailed step analysis** - Inspect request/response data, timing, and errors for each step
- **Token usage insights** - Track prompt and completion tokens across all requests
- **Error debugging** - Easily identify and debug failed requests with full error details
- **Multi-run comparison** - Compare different SDK runs side-by-side
- **Dark/Light mode** - Full theme support with automatic system preference detection

![DevTools Interface](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/c42509db3b19a615dbca8c54a76514ef70ad33ee9f814a0546c2188b90bbfc54/content/assets/sdk-devtools-dark.png)

### SDK Telemetry Hooks

Developer-friendly hooks that automatically capture:

- All chat completions with full request/response data
- Token usage and costs
- Timing information for performance analysis
- Errors and failure modes
- Tool/function calls
- Current directory, git branch, and model information

## Installation

Install the DevTools package as a development dependency:

```
|  |  |
| --- | --- |
| $ | npm install @openrouter/devtools --save-dev |
```

**Important:** DevTools is designed for development only. It will throw an error if `NODE_ENV === 'production'` to prevent accidental production deployment.

## Quick Start - SDK Hooks

Integrate DevTools hooks into your SDK client to start capturing telemetry:

### Basic Usage

```
|  |  |
| --- | --- |
| 1 | import { createOpenRouterDevtools } from '@openrouter/devtools'; |
| 2 | import { OpenRouter } from '@openrouter/sdk'; |
| 3 |  |
| 4 | const sdk = new OpenRouter({ |
| 5 | apiKey: process.env.OPENROUTER_API_KEY, |
| 6 | hooks: createOpenRouterDevtools() |
| 7 | }); |
| 8 |  |
| 9 | // Now all SDK operations are automatically captured |
| 10 | const response = await sdk.chat.send({ |
| 11 | model: "openai/gpt-5", |
| 12 | messages: [ |
| 13 | { role: "user", content: "Explain quantum computing" } |
| 14 | ] |
| 15 | }); |
```

### Custom Configuration

```
|  |  |
| --- | --- |
| 1 | const sdk = new OpenRouter({ |
| 2 | apiKey: process.env.OPENROUTER_API_KEY, |
| 3 | hooks: createOpenRouterDevtools({ |
| 4 | storagePath: '.custom-path/generations.json',  // Default: '.devtools/openrouter-generations.json' |
| 5 | serverUrl: 'http://localhost:5000/api/notify', // Default: 'http://localhost:4983/api/notify' |
| 6 | }) |
| 7 | }); |
```

## Quick Start - DevTools Viewer

Launch the DevTools web interface to visualize captured telemetry:

```
|  |  |
| --- | --- |
| $ | openrouter devtools |
```

This starts a local server on port 4983 and opens your browser to view:

- All SDK runs with timestamps and status
- Step-by-step request/response details
- Token usage and costs
- Error messages and stack traces
- Performance timing information

The viewer automatically refreshes when new telemetry data is captured.

## How It Works

### Telemetry Capture Flow

1. SDK hooks intercept requests before they’re sent
2. Telemetry data is captured asynchronously (non-blocking)
3. Data is stored in `.devtools/openrouter-generations.json`
4. A notification is sent to the local DevTools server (if running)
5. The DevTools viewer updates in real-time

### Non-Intrusive Design

- **Zero SDK impact** - Telemetry capture is async and never blocks SDK operations
- **Graceful degradation** - Errors in DevTools never break your SDK calls
- **Development-only** - Throws error if used in production (`NODE_ENV === 'production'`)

### Storage Location

By default, telemetry is stored in:

```
|  |
| --- |
| .devtools/openrouter-generations.json |
```

This file contains:

- **Runs** - Top-level tracking of SDK operations
- **Steps** - Individual request/response pairs within each run
- **Metadata** - Timestamps, status, token usage, errors

## Configuration Options

### Hook Configuration

When calling `createOpenRouterDevtools()`, you can customize:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `storagePath` | `string` | `'.devtools/openrouter-generations.json'` | Where to store captured telemetry |
| `serverUrl` | `string` | `'http://localhost:4983/api/notify'` | DevTools server notification endpoint |

### DevTools Server Configuration

The DevTools viewer runs on port 4983 by default. This can be configured in your OpenRouter CLI configuration at `~/.openrouter/claude-code-proxy.json`:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "DEVTOOLS_PORT": 4983 |
| 3 | } |
```

## Operations Captured

The DevTools hooks automatically capture these SDK operations:

- `chat.send()` - Chat completions API calls
- `chat.createResponses()` - Responses API calls
- `embeddings.create()` - Embeddings API calls

All other SDK operations are currently ignored.

## Data Captured Per Step

For each SDK operation, DevTools captures:

**Request Data:**

- Model name
- Messages/prompts
- Parameters (temperature, max\_tokens, etc.)

**Response Data:**

- Generated content
- Token usage (prompt + completion tokens)
- Provider and model used
- Finish reason
- Tool calls (if any)

**Metadata:**

- Start and completion timestamps
- Duration in milliseconds
- Status (success, error, in\_progress)
- Error details (if failed)

## Safety & Best Practices

### Production Environment Protection

DevTools will throw an error if initialized when `NODE_ENV === 'production'`:

```
|  |  |
| --- | --- |
| 1 | // This will throw an error in production |
| 2 | const sdk = new OpenRouter({ |
| 3 | apiKey: process.env.OPENROUTER_API_KEY, |
| 4 | hooks: createOpenRouterDevtools() // ERROR in production! |
| 5 | }); |
```

### Non-Blocking Architecture

- All telemetry capture happens asynchronously
- DevTools errors never propagate to your SDK calls
- Failed writes are logged but don’t break your application

### Error Handling

DevTools failures are handled gracefully:

```
|  |  |
| --- | --- |
| 1 | // If DevTools fails, your SDK call still works |
| 2 | try { |
| 3 | await sdk.chat.send({ /* ... */ }); |
| 4 | // SDK call succeeds even if DevTools capture fails |
| 5 | } catch (error) { |
| 6 | // Only SDK errors are thrown, never DevTools errors |
| 7 | } |
```

## Troubleshooting

### Port Already in Use

If port 4983 is already in use:

```
|  |  |
| --- | --- |
| $ | Error: listen EADDRINUSE: address already in use :::4983 |
```

**Solution:** Either stop the process using port 4983, or configure a different port in `~/.openrouter/claude-code-proxy.json`:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "DEVTOOLS_PORT": 5000 |
| 3 | } |
```

Then update your hook configuration:

```
|  |  |
| --- | --- |
| 1 | hooks: createOpenRouterDevtools({ |
| 2 | serverUrl: 'http://localhost:5000/api/notify' |
| 3 | }) |
```

### Storage Location Issues

If you can’t find the telemetry file:

1. Check the default location: `.devtools/openrouter-generations.json`
2. Ensure you have write permissions in your working directory
3. Check for custom `storagePath` configuration

### DevTools Viewer Not Updating

If the viewer doesn’t show new requests:

1. Verify the DevTools server is running (`openrouter devtools`)
2. Check that `serverUrl` matches the DevTools server port
3. Ensure the telemetry file is being written (check `.devtools/` directory)
4. Try refreshing the browser manually

### Common Setup Issues

**Issue:** DevTools package not found

```
|  |  |
| --- | --- |
| $ | Cannot find module '@openrouter/devtools' |
```

**Solution:** Install the package:

```
|  |  |
| --- | --- |
| $ | npm install @openrouter/devtools --save-dev |
```

---

**Issue:** Accidental production usage

```
|  |  |
| --- | --- |
| $ | Error: DevTools should not be used in production |
```

**Solution:** Only initialize DevTools in development:

```
|  |  |
| --- | --- |
| 1 | const hooks = process.env.NODE_ENV === 'development' |
| 2 | ? createOpenRouterDevtools() |
| 3 | : undefined; |
| 4 |  |
| 5 | const sdk = new OpenRouter({ |
| 6 | apiKey: process.env.OPENROUTER_API_KEY, |
| 7 | hooks |
| 8 | }); |
```
