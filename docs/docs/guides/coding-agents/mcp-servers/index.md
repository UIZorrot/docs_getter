---
source_url: "https://openrouter.ai/docs/guides/coding-agents/mcp-servers"
title: "Using MCP Servers with OpenRouter | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:33.267662+00:00"
---
[Guides](../../administration/activity-export/index.md)[Coding Agents](../automatic-code-review/index.md)

# Using MCP Servers with OpenRouter

Use MCP Servers with OpenRouter

MCP servers are a popular way of providing LLMs with tool calling abilities, and are an alternative to using OpenAI-compatible tool calling.

By converting MCP (Anthropic) tool definitions to OpenAI-compatible tool definitions, you can use MCP servers with OpenRouter.

In this example, we’ll use [Anthropic’s MCP client SDK](https://github.com/modelcontextprotocol/python-sdk) to interact with the File System MCP, all with OpenRouter under the hood.

##### 

Note that interacting with MCP servers is more complex than calling a REST
endpoint. The MCP protocol is stateful and requires session management. The
example below uses the MCP client SDK, but is still somewhat complex.

First, some setup. In order to run this you will need to pip install the packages, and create a `.env` file with OPENAI\_API\_KEY set. This example also assumes the directory `/Applications` exists.

```
|  |  |
| --- | --- |
| 1 | import asyncio |
| 2 | from typing import Optional |
| 3 | from contextlib import AsyncExitStack |
| 4 |  |
| 5 | from mcp import ClientSession, StdioServerParameters |
| 6 | from mcp.client.stdio import stdio_client |
| 7 |  |
| 8 | from openai import OpenAI |
| 9 | from dotenv import load_dotenv |
| 10 | import json |
| 11 |  |
| 12 | load_dotenv()  # load environment variables from .env |
| 13 |  |
| 14 | MODEL = "anthropic/claude-3-7-sonnet" |
| 15 |  |
| 16 | SERVER_CONFIG = { |
| 17 | "command": "npx", |
| 18 | "args": ["-y", |
| 19 | "@modelcontextprotocol/server-filesystem", |
| 20 | f"/Applications/"], |
| 21 | "env": None |
| 22 | } |
```

Next, our helper function to convert MCP tool definitions to OpenAI tool definitions:

```
|  |  |
| --- | --- |
| 1 | def convert_tool_format(tool): |
| 2 | converted_tool = { |
| 3 | "type": "function", |
| 4 | "function": { |
| 5 | "name": tool.name, |
| 6 | "description": tool.description, |
| 7 | "parameters": { |
| 8 | "type": "object", |
| 9 | "properties": tool.inputSchema["properties"], |
| 10 | "required": tool.inputSchema["required"] |
| 11 | } |
| 12 | } |
| 13 | } |
| 14 | return converted_tool |
```

And, the MCP client itself; a regrettable ~100 lines of code. Note that the SERVER\_CONFIG is hard-coded into the client, but of course could be parameterized for other MCP servers.

```
|  |  |
| --- | --- |
| 1 | class MCPClient: |
| 2 | def __init__(self): |
| 3 | self.session: Optional[ClientSession] = None |
| 4 | self.exit_stack = AsyncExitStack() |
| 5 | self.openai = OpenAI( |
| 6 | base_url="https://openrouter.ai/api/v1" |
| 7 | ) |
| 8 |  |
| 9 | async def connect_to_server(self, server_config): |
| 10 | server_params = StdioServerParameters(**server_config) |
| 11 | stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params)) |
| 12 | self.stdio, self.write = stdio_transport |
| 13 | self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write)) |
| 14 |  |
| 15 | await self.session.initialize() |
| 16 |  |
| 17 | # List available tools from the MCP server |
| 18 | response = await self.session.list_tools() |
| 19 | print("\nConnected to server with tools:", [tool.name for tool in response.tools]) |
| 20 |  |
| 21 | self.messages = [] |
| 22 |  |
| 23 | async def process_query(self, query: str) -> str: |
| 24 |  |
| 25 | self.messages.append({ |
| 26 | "role": "user", |
| 27 | "content": query |
| 28 | }) |
| 29 |  |
| 30 | response = await self.session.list_tools() |
| 31 | available_tools = [convert_tool_format(tool) for tool in response.tools] |
| 32 |  |
| 33 | response = self.openai.chat.completions.create( |
| 34 | model=MODEL, |
| 35 | tools=available_tools, |
| 36 | messages=self.messages |
| 37 | ) |
| 38 | self.messages.append(response.choices[0].message.model_dump()) |
| 39 |  |
| 40 | final_text = [] |
| 41 | content = response.choices[0].message |
| 42 | if content.tool_calls is not None: |
| 43 | tool_name = content.tool_calls[0].function.name |
| 44 | tool_args = content.tool_calls[0].function.arguments |
| 45 | tool_args = json.loads(tool_args) if tool_args else {} |
| 46 |  |
| 47 | # Execute tool call |
| 48 | try: |
| 49 | result = await self.session.call_tool(tool_name, tool_args) |
| 50 | final_text.append(f"[Calling tool {tool_name} with args {tool_args}]") |
| 51 | except Exception as e: |
| 52 | print(f"Error calling tool {tool_name}: {e}") |
| 53 | result = None |
| 54 |  |
| 55 | self.messages.append({ |
| 56 | "role": "tool", |
| 57 | "tool_call_id": content.tool_calls[0].id, |
| 58 | "name": tool_name, |
| 59 | "content": result.content |
| 60 | }) |
| 61 |  |
| 62 | response = self.openai.chat.completions.create( |
| 63 | model=MODEL, |
| 64 | max_tokens=1000, |
| 65 | messages=self.messages, |
| 66 | ) |
| 67 |  |
| 68 | final_text.append(response.choices[0].message.content) |
| 69 | else: |
| 70 | final_text.append(content.content) |
| 71 |  |
| 72 | return "\n".join(final_text) |
| 73 |  |
| 74 | async def chat_loop(self): |
| 75 | """Run an interactive chat loop""" |
| 76 | print("\nMCP Client Started!") |
| 77 | print("Type your queries or 'quit' to exit.") |
| 78 |  |
| 79 | while True: |
| 80 | try: |
| 81 | query = input("\nQuery: ").strip() |
| 82 | result = await self.process_query(query) |
| 83 | print("Result:") |
| 84 | print(result) |
| 85 |  |
| 86 | except Exception as e: |
| 87 | print(f"Error: {str(e)}") |
| 88 |  |
| 89 | async def cleanup(self): |
| 90 | await self.exit_stack.aclose() |
| 91 |  |
| 92 | async def main(): |
| 93 | client = MCPClient() |
| 94 | try: |
| 95 | await client.connect_to_server(SERVER_CONFIG) |
| 96 | await client.chat_loop() |
| 97 | finally: |
| 98 | await client.cleanup() |
| 99 |  |
| 100 | if __name__ == "__main__": |
| 101 | import sys |
| 102 | asyncio.run(main()) |
```

Assembling all of the above code into mcp-client.py, you get a client that behaves as follows (some outputs truncated for brevity):

```
|  |  |
| --- | --- |
| $ | % python mcp-client.py |
| $ |  |
| $ | Secure MCP Filesystem Server running on stdio |
| $ | Allowed directories: [ '/Applications' ] |
| $ |  |
| $ | Connected to server with tools: ['read_file', 'read_multiple_files', 'write_file'...] |
| $ |  |
| $ | MCP Client Started! |
| $ | Type your queries or 'quit' to exit. |
| $ |  |
| $ | Query: Do I have microsoft office installed? |
| $ |  |
| $ | Result: |
| $ | [Calling tool list_allowed_directories with args {}] |
| $ | I can check if Microsoft Office is installed in the Applications folder: |
| $ |  |
| $ | Query: continue |
| $ |  |
| $ | Result: |
| $ | [Calling tool search_files with args {'path': '/Applications', 'pattern': 'Microsoft'}] |
| $ | Now let me check specifically for Microsoft Office applications: |
| $ |  |
| $ | Query: continue |
| $ |  |
| $ | Result: |
| $ | I can see from the search results that Microsoft Office is indeed installed on your system. |
| $ | The search found the following main Microsoft Office applications: |
| $ |  |
| $ | 1. Microsoft Excel - /Applications/Microsoft Excel.app |
| $ | 2. Microsoft PowerPoint - /Applications/Microsoft PowerPoint.app |
| $ | 3. Microsoft Word - /Applications/Microsoft Word.app |
| $ | 4. OneDrive - /Applications/OneDrive.app (which includes Microsoft SharePoint integration) |
```
