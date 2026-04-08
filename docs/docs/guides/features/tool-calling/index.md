---
source_url: "https://openrouter.ai/docs/guides/features/tool-calling"
title: "Tool & Function Calling | Use Tools with OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:39.911102+00:00"
---
[Features](../presets/index.md)

# 

Tool & Function Calling

Use tools in your prompts

Tool calls (also known as function calls) give an LLM access to external tools. The LLM does not call the tools directly. Instead, it suggests the tool to call. The user then calls the tool separately and provides the results back to the LLM. Finally, the LLM formats the response into an answer to the user’s original question.

OpenRouter standardizes the tool calling interface across models and providers, making it easy to integrate external tools with any supported model.

**Supported Models**: You can find models that support tool calling by filtering on [openrouter.ai/models?supported\_parameters=tools](https://openrouter.ai/models).

If you prefer to learn from a full end-to-end example, keep reading.

## Request Body Examples

Tool calling with OpenRouter involves three key steps. Here are the essential request body formats for each step:

### Step 1: Inference Request with Tools

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "google/gemini-3-flash-preview", |
| 3 | "messages": [ |
| 4 | { |
| 5 | "role": "user", |
| 6 | "content": "What are the titles of some James Joyce books?" |
| 7 | } |
| 8 | ], |
| 9 | "tools": [ |
| 10 | { |
| 11 | "type": "function", |
| 12 | "function": { |
| 13 | "name": "search_gutenberg_books", |
| 14 | "description": "Search for books in the Project Gutenberg library", |
| 15 | "parameters": { |
| 16 | "type": "object", |
| 17 | "properties": { |
| 18 | "search_terms": { |
| 19 | "type": "array", |
| 20 | "items": {"type": "string"}, |
| 21 | "description": "List of search terms to find books" |
| 22 | } |
| 23 | }, |
| 24 | "required": ["search_terms"] |
| 25 | } |
| 26 | } |
| 27 | } |
| 28 | ] |
| 29 | } |
```

### Step 2: Tool Execution (Client-Side)

After receiving the model’s response with `tool_calls`, execute the requested tool locally and prepare the result:

```
|  |  |
| --- | --- |
| 1 | // Model responds with tool_calls, you execute the tool locally |
| 2 | const toolResult = await searchGutenbergBooks(["James", "Joyce"]); |
```

### Step 3: Inference Request with Tool Results

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "google/gemini-3-flash-preview", |
| 3 | "messages": [ |
| 4 | { |
| 5 | "role": "user", |
| 6 | "content": "What are the titles of some James Joyce books?" |
| 7 | }, |
| 8 | { |
| 9 | "role": "assistant", |
| 10 | "content": null, |
| 11 | "tool_calls": [ |
| 12 | { |
| 13 | "id": "call_abc123", |
| 14 | "type": "function", |
| 15 | "function": { |
| 16 | "name": "search_gutenberg_books", |
| 17 | "arguments": "{\"search_terms\": [\"James\", \"Joyce\"]}" |
| 18 | } |
| 19 | } |
| 20 | ] |
| 21 | }, |
| 22 | { |
| 23 | "role": "tool", |
| 24 | "tool_call_id": "call_abc123", |
| 25 | "content": "[{\"id\": 4300, \"title\": \"Ulysses\", \"authors\": [{\"name\": \"Joyce, James\"}]}]" |
| 26 | } |
| 27 | ], |
| 28 | "tools": [ |
| 29 | { |
| 30 | "type": "function", |
| 31 | "function": { |
| 32 | "name": "search_gutenberg_books", |
| 33 | "description": "Search for books in the Project Gutenberg library", |
| 34 | "parameters": { |
| 35 | "type": "object", |
| 36 | "properties": { |
| 37 | "search_terms": { |
| 38 | "type": "array", |
| 39 | "items": {"type": "string"}, |
| 40 | "description": "List of search terms to find books" |
| 41 | } |
| 42 | }, |
| 43 | "required": ["search_terms"] |
| 44 | } |
| 45 | } |
| 46 | } |
| 47 | ] |
| 48 | } |
```

**Note**: The `tools` parameter must be included in every request (Steps 1 and 3) so the router can validate the tool schema on each call.

### Tool Calling Example

Here is Python code that gives LLMs the ability to call an external API — in this case Project Gutenberg, to search for books.

First, let’s do some basic setup:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter } from '@openrouter/sdk'; |
| 2 |  |
| 3 | const OPENROUTER_API_KEY = "{{API_KEY_REF}}"; |
| 4 |  |
| 5 | // You can use any model that supports tool calling |
| 6 | const MODEL = "{{MODEL}}"; |
| 7 |  |
| 8 | const openRouter = new OpenRouter({ |
| 9 | apiKey: OPENROUTER_API_KEY, |
| 10 | }); |
| 11 |  |
| 12 | const task = "What are the titles of some James Joyce books?"; |
| 13 |  |
| 14 | const messages = [ |
| 15 | { |
| 16 | role: "system", |
| 17 | content: "You are a helpful assistant." |
| 18 | }, |
| 19 | { |
| 20 | role: "user", |
| 21 | content: task, |
| 22 | } |
| 23 | ]; |
```

### Define the Tool

Next, we define the tool that we want to call. Remember, the tool is going to get *requested* by the LLM, but the code we are writing here is ultimately responsible for executing the call and returning the results to the LLM.

```
|  |  |
| --- | --- |
| 1 | async function searchGutenbergBooks(searchTerms: string[]): Promise<Book[]> { |
| 2 | const searchQuery = searchTerms.join(' '); |
| 3 | const url = 'https://gutendex.com/books'; |
| 4 | const response = await fetch(`${url}?search=${searchQuery}`); |
| 5 | const data = await response.json(); |
| 6 |  |
| 7 | return data.results.map((book: any) => ({ |
| 8 | id: book.id, |
| 9 | title: book.title, |
| 10 | authors: book.authors, |
| 11 | })); |
| 12 | } |
| 13 |  |
| 14 | const tools = [ |
| 15 | { |
| 16 | type: 'function', |
| 17 | function: { |
| 18 | name: 'searchGutenbergBooks', |
| 19 | description: |
| 20 | 'Search for books in the Project Gutenberg library based on specified search terms', |
| 21 | parameters: { |
| 22 | type: 'object', |
| 23 | properties: { |
| 24 | search_terms: { |
| 25 | type: 'array', |
| 26 | items: { |
| 27 | type: 'string', |
| 28 | }, |
| 29 | description: |
| 30 | "List of search terms to find books in the Gutenberg library (e.g. ['dickens', 'great'] to search for books by Dickens with 'great' in the title)", |
| 31 | }, |
| 32 | }, |
| 33 | required: ['search_terms'], |
| 34 | }, |
| 35 | }, |
| 36 | }, |
| 37 | ]; |
| 38 |  |
| 39 | const TOOL_MAPPING = { |
| 40 | searchGutenbergBooks, |
| 41 | }; |
```

Note that the “tool” is just a normal function. We then write a JSON “spec” compatible with the OpenAI function calling parameter. We’ll pass that spec to the LLM so that it knows this tool is available and how to use it. It will request the tool when needed, along with any arguments. We’ll then marshal the tool call locally, make the function call, and return the results to the LLM.

### Tool use and tool results

Let’s make the first OpenRouter API call to the model:

```
|  |  |
| --- | --- |
| 1 | const result = await openRouter.chat.send({ |
| 2 | model: '{{MODEL}}', |
| 3 | tools, |
| 4 | messages, |
| 5 | stream: false, |
| 6 | }); |
| 7 |  |
| 8 | const response_1 = result.choices[0].message; |
```

The LLM responds with a finish reason of `tool_calls`, and a `tool_calls` array. In a generic LLM response-handler, you would want to check the `finish_reason` before processing tool calls, but here we will assume it’s the case. Let’s keep going, by processing the tool call:

```
|  |  |
| --- | --- |
| 1 | // Append the response to the messages array so the LLM has the full context |
| 2 | // It's easy to forget this step! |
| 3 | messages.push(response_1); |
| 4 |  |
| 5 | // Now we process the requested tool calls, and use our book lookup tool |
| 6 | for (const toolCall of response_1.tool_calls) { |
| 7 | const toolName = toolCall.function.name; |
| 8 | const { search_params } = JSON.parse(toolCall.function.arguments); |
| 9 | const toolResponse = await TOOL_MAPPING[toolName](search_params); |
| 10 | messages.push({ |
| 11 | role: 'tool', |
| 12 | toolCallId: toolCall.id, |
| 13 | name: toolName, |
| 14 | content: JSON.stringify(toolResponse), |
| 15 | }); |
| 16 | } |
```

The messages array now has:

1. Our original request
2. The LLM’s response (containing a tool call request)
3. The result of the tool call (a json object returned from the Project Gutenberg API)

Now, we can make a second OpenRouter API call, and hopefully get our result!

```
|  |  |
| --- | --- |
| 1 | const response_2 = await openRouter.chat.send({ |
| 2 | model: '{{MODEL}}', |
| 3 | messages, |
| 4 | tools, |
| 5 | stream: false, |
| 6 | }); |
| 7 |  |
| 8 | console.log(response_2.choices[0].message.content); |
```

The output will be something like:

```
|  |
| --- |
| Here are some books by James Joyce: |
|  |
| *   *Ulysses* |
| *   *Dubliners* |
| *   *A Portrait of the Artist as a Young Man* |
| *   *Chamber Music* |
| *   *Exiles: A Play in Three Acts* |
```

We did it! We’ve successfully used a tool in a prompt.

## Interleaved Thinking

Interleaved thinking allows models to reason between tool calls, enabling more sophisticated decision-making after receiving tool results. This feature helps models chain multiple tool calls with reasoning steps in between and make nuanced decisions based on intermediate results.

**Important**: Interleaved thinking increases token usage and response latency. Consider your budget and performance requirements when enabling this feature.

### How Interleaved Thinking Works

With interleaved thinking, the model can:

- Reason about the results of a tool call before deciding what to do next
- Chain multiple tool calls with reasoning steps in between
- Make more nuanced decisions based on intermediate results
- Provide transparent reasoning for its tool selection process

### Example: Multi-Step Research with Reasoning

Here’s an example showing how a model might use interleaved thinking to research a topic across multiple sources:

**Initial Request:**

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "anthropic/claude-sonnet-4.5", |
| 3 | "messages": [ |
| 4 | { |
| 5 | "role": "user", |
| 6 | "content": "Research the environmental impact of electric vehicles and provide a comprehensive analysis." |
| 7 | } |
| 8 | ], |
| 9 | "tools": [ |
| 10 | { |
| 11 | "type": "function", |
| 12 | "function": { |
| 13 | "name": "search_academic_papers", |
| 14 | "description": "Search for academic papers on a given topic", |
| 15 | "parameters": { |
| 16 | "type": "object", |
| 17 | "properties": { |
| 18 | "query": {"type": "string"}, |
| 19 | "field": {"type": "string"} |
| 20 | }, |
| 21 | "required": ["query"] |
| 22 | } |
| 23 | } |
| 24 | }, |
| 25 | { |
| 26 | "type": "function", |
| 27 | "function": { |
| 28 | "name": "get_latest_statistics", |
| 29 | "description": "Get latest statistics on a topic", |
| 30 | "parameters": { |
| 31 | "type": "object", |
| 32 | "properties": { |
| 33 | "topic": {"type": "string"}, |
| 34 | "year": {"type": "integer"} |
| 35 | }, |
| 36 | "required": ["topic"] |
| 37 | } |
| 38 | } |
| 39 | } |
| 40 | ] |
| 41 | } |
```

**Model’s Reasoning and Tool Calls:**

1. **Initial Thinking**: “I need to research electric vehicle environmental impact. Let me start with academic papers to get peer-reviewed research.”
2. **First Tool Call**: `search_academic_papers({"query": "electric vehicle lifecycle environmental impact", "field": "environmental science"})`
3. **After First Tool Result**: “The papers show mixed results on manufacturing impact. I need current statistics to complement this academic research.”
4. **Second Tool Call**: `get_latest_statistics({"topic": "electric vehicle carbon footprint", "year": 2024})`
5. **After Second Tool Result**: “Now I have both academic research and current data. Let me search for manufacturing-specific studies to address the gaps I found.”
6. **Third Tool Call**: `search_academic_papers({"query": "electric vehicle battery manufacturing environmental cost", "field": "materials science"})`
7. **Final Analysis**: Synthesizes all gathered information into a comprehensive response.

### Best Practices for Interleaved Thinking

- **Clear Tool Descriptions**: Provide detailed descriptions so the model can reason about when to use each tool
- **Structured Parameters**: Use well-defined parameter schemas to help the model make precise tool calls
- **Context Preservation**: Maintain conversation context across multiple tool interactions
- **Error Handling**: Design tools to provide meaningful error messages that help the model adjust its approach

### Implementation Considerations

When implementing interleaved thinking:

- Models may take longer to respond due to additional reasoning steps
- Token usage will be higher due to the reasoning process
- The quality of reasoning depends on the model’s capabilities
- Some models may be better suited for this approach than others

## A Simple Agentic Loop

In the example above, the calls are made explicitly and sequentially. To handle a wide variety of user inputs and tool calls, you can use an agentic loop.

Here’s an example of a simple agentic loop (using the same `tools` and initial `messages` as above):

```
|  |  |
| --- | --- |
| 1 | async function callLLM(messages: Message[]): Promise<ChatResponse> { |
| 2 | const result = await openRouter.chat.send({ |
| 3 | model: '{{MODEL}}', |
| 4 | tools, |
| 5 | messages, |
| 6 | stream: false, |
| 7 | }); |
| 8 |  |
| 9 | messages.push(result.choices[0].message); |
| 10 | return result; |
| 11 | } |
| 12 |  |
| 13 | async function getToolResponse(response: ChatResponse): Promise<Message> { |
| 14 | const toolCall = response.choices[0].message.toolCalls[0]; |
| 15 | const toolName = toolCall.function.name; |
| 16 | const toolArgs = JSON.parse(toolCall.function.arguments); |
| 17 |  |
| 18 | // Look up the correct tool locally, and call it with the provided arguments |
| 19 | // Other tools can be added without changing the agentic loop |
| 20 | const toolResult = await TOOL_MAPPING[toolName](toolArgs); |
| 21 |  |
| 22 | return { |
| 23 | role: 'tool', |
| 24 | toolCallId: toolCall.id, |
| 25 | content: toolResult, |
| 26 | }; |
| 27 | } |
| 28 |  |
| 29 | const maxIterations = 10; |
| 30 | let iterationCount = 0; |
| 31 |  |
| 32 | while (iterationCount < maxIterations) { |
| 33 | iterationCount++; |
| 34 | const response = await callLLM(messages); |
| 35 |  |
| 36 | if (response.choices[0].message.toolCalls) { |
| 37 | messages.push(await getToolResponse(response)); |
| 38 | } else { |
| 39 | break; |
| 40 | } |
| 41 | } |
| 42 |  |
| 43 | if (iterationCount >= maxIterations) { |
| 44 | console.warn("Warning: Maximum iterations reached"); |
| 45 | } |
| 46 |  |
| 47 | console.log(messages[messages.length - 1].content); |
```

## Best Practices and Advanced Patterns

### Function Definition Guidelines

When defining tools for LLMs, follow these best practices:

**Clear and Descriptive Names**: Use descriptive function names that clearly indicate the tool’s purpose.

```
|  |  |
| --- | --- |
| 1 | // Good: Clear and specific |
| 2 | { "name": "get_weather_forecast" } |
```

```
|  |  |
| --- | --- |
| 1 | // Avoid: Too vague |
| 2 | { "name": "weather" } |
```

**Comprehensive Descriptions**: Provide detailed descriptions that help the model understand when and how to use the tool.

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "description": "Get current weather conditions and 5-day forecast for a specific location. Supports cities, zip codes, and coordinates.", |
| 3 | "parameters": { |
| 4 | "type": "object", |
| 5 | "properties": { |
| 6 | "location": { |
| 7 | "type": "string", |
| 8 | "description": "City name, zip code, or coordinates (lat,lng). Examples: 'New York', '10001', '40.7128,-74.0060'" |
| 9 | }, |
| 10 | "units": { |
| 11 | "type": "string", |
| 12 | "enum": ["celsius", "fahrenheit"], |
| 13 | "description": "Temperature unit preference", |
| 14 | "default": "celsius" |
| 15 | } |
| 16 | }, |
| 17 | "required": ["location"] |
| 18 | } |
| 19 | } |
```

### Streaming with Tool Calls

When using streaming responses with tool calls, handle the different content types appropriately:

```
|  |  |
| --- | --- |
| 1 | const stream = await fetch('/api/chat/completions', { |
| 2 | method: 'POST', |
| 3 | headers: { 'Content-Type': 'application/json' }, |
| 4 | body: JSON.stringify({ |
| 5 | model: 'anthropic/claude-sonnet-4.5', |
| 6 | messages: messages, |
| 7 | tools: tools, |
| 8 | stream: true |
| 9 | }) |
| 10 | }); |
| 11 |  |
| 12 | const reader = stream.body.getReader(); |
| 13 | let toolCalls = []; |
| 14 |  |
| 15 | while (true) { |
| 16 | const { done, value } = await reader.read(); |
| 17 | if (done) { |
| 18 | break; |
| 19 | } |
| 20 |  |
| 21 | const chunk = new TextDecoder().decode(value); |
| 22 | const lines = chunk.split('\n').filter(line => line.trim()); |
| 23 |  |
| 24 | for (const line of lines) { |
| 25 | if (line.startsWith('data: ')) { |
| 26 | const data = JSON.parse(line.slice(6)); |
| 27 |  |
| 28 | if (data.choices[0].delta.tool_calls) { |
| 29 | toolCalls.push(...data.choices[0].delta.tool_calls); |
| 30 | } |
| 31 |  |
| 32 | if (data.choices[0].delta.finish_reason === 'tool_calls') { |
| 33 | await handleToolCalls(toolCalls); |
| 34 | } else if (data.choices[0].delta.finish_reason === 'stop') { |
| 35 | // Regular completion without tool calls |
| 36 | break; |
| 37 | } |
| 38 | } |
| 39 | } |
| 40 | } |
```

### Tool Choice Configuration

Control tool usage with the `tool_choice` parameter:

```
|  |  |
| --- | --- |
| 1 | // Let model decide (default) |
| 2 | { "tool_choice": "auto" } |
```

```
|  |  |
| --- | --- |
| 1 | // Disable tool usage |
| 2 | { "tool_choice": "none" } |
```

```
|  |  |
| --- | --- |
| 1 | // Force specific tool |
| 2 | { |
| 3 | "tool_choice": { |
| 4 | "type": "function", |
| 5 | "function": {"name": "search_database"} |
| 6 | } |
| 7 | } |
```

### Parallel Tool Calls

Control whether multiple tools can be called simultaneously with the `parallel_tool_calls` parameter (default is true for most models):

```
|  |  |
| --- | --- |
| 1 | // Disable parallel tool calls - tools will be called sequentially |
| 2 | { "parallel_tool_calls": false } |
```

When `parallel_tool_calls` is `false`, the model will only request one tool call at a time instead of potentially multiple calls in parallel.

### Multi-Tool Workflows

Design tools that work well together:

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "tools": [ |
| 3 | { |
| 4 | "type": "function", |
| 5 | "function": { |
| 6 | "name": "search_products", |
| 7 | "description": "Search for products in the catalog" |
| 8 | } |
| 9 | }, |
| 10 | { |
| 11 | "type": "function", |
| 12 | "function": { |
| 13 | "name": "get_product_details", |
| 14 | "description": "Get detailed information about a specific product" |
| 15 | } |
| 16 | }, |
| 17 | { |
| 18 | "type": "function", |
| 19 | "function": { |
| 20 | "name": "check_inventory", |
| 21 | "description": "Check current inventory levels for a product" |
| 22 | } |
| 23 | } |
| 24 | ] |
| 25 | } |
```

This allows the model to naturally chain operations: search → get details → check inventory.

For more details on OpenRouter’s message format and tool parameters, see the [API Reference](../../../api-reference/overview/index.md).
