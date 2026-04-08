---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/examples/skills-loader"
title: "Skills Loader Example | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:48.867324+00:00"
---
[TypeScript SDK](../../../overview/index.md)[Call Model](../../overview/index.md)[Examples](../weather-tool/index.md)

# Skills Loader

A complete implementation of a skills system similar to Claude Code, demonstrating the power of `nextTurnParams` for context injection.

## Overview

This example shows how to build encapsulated, self-managing tools that inject domain-specific context into conversations. When a skill is loaded, it automatically enriches subsequent turns with specialized instructions.

## Prerequisites

```
|  |  |
| --- | --- |
| $ | pnpm add @openrouter/sdk zod |
```

Create a skills directory:

```
|  |  |
| --- | --- |
| $ | mkdir -p ~/.claude/skills/pdf-processing |
| $ | mkdir -p ~/.claude/skills/data-analysis |
| $ | mkdir -p ~/.claude/skills/code-review |
```

## Basic Skills Tool

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter, tool } from '@openrouter/agent'; |
| 2 | import { readFileSync, existsSync, readdirSync } from 'fs'; |
| 3 | import path from 'path'; |
| 4 | import { z } from 'zod'; |
| 5 |  |
| 6 | const openrouter = new OpenRouter({ |
| 7 | apiKey: process.env.OPENROUTER_API_KEY, |
| 8 | }); |
| 9 |  |
| 10 | const SKILLS_DIR = path.join(process.env.HOME || '~', '.claude', 'skills'); |
| 11 |  |
| 12 | // List available skills |
| 13 | const listAvailableSkills = (): string[] => { |
| 14 | if (!existsSync(SKILLS_DIR)) return []; |
| 15 | return readdirSync(SKILLS_DIR, { withFileTypes: true }) |
| 16 | .filter((dirent) => dirent.isDirectory()) |
| 17 | .filter((dirent) => existsSync(path.join(SKILLS_DIR, dirent.name, 'SKILL.md'))) |
| 18 | .map((dirent) => dirent.name); |
| 19 | }; |
| 20 |  |
| 21 | const skillsTool = tool({ |
| 22 | name: 'Skill', |
| 23 | description: `Load a specialized skill to enhance the assistant's capabilities. |
| 24 | Available skills: ${listAvailableSkills().join(', ') || 'none configured'} |
| 25 | Each skill provides domain-specific instructions and capabilities.`, |
| 26 |  |
| 27 | inputSchema: z.object({ |
| 28 | type: z.string().describe("The skill type to load (e.g., 'pdf-processing')"), |
| 29 | }), |
| 30 |  |
| 31 | outputSchema: z.string(), |
| 32 |  |
| 33 | // This is where the magic happens - modify context for next turn |
| 34 | nextTurnParams: { |
| 35 | input: (params, context) => { |
| 36 | // Prevent duplicate skill loading |
| 37 | const skillMarker = `[Skill: ${params.type}]`; |
| 38 | if (JSON.stringify(context.input).includes(skillMarker)) { |
| 39 | return context.input; |
| 40 | } |
| 41 |  |
| 42 | // Load the skill's instructions |
| 43 | const skillPath = path.join(SKILLS_DIR, params.type, 'SKILL.md'); |
| 44 | if (!existsSync(skillPath)) { |
| 45 | return context.input; |
| 46 | } |
| 47 |  |
| 48 | const skill = readFileSync(skillPath, 'utf-8'); |
| 49 | const skillDir = path.join(SKILLS_DIR, params.type); |
| 50 |  |
| 51 | // Inject skill context into the conversation |
| 52 | const currentInput = Array.isArray(context.input) ? context.input : [context.input]; |
| 53 |  |
| 54 | return [ |
| 55 | ...currentInput, |
| 56 | { |
| 57 | role: 'user', |
| 58 | content: `${skillMarker} |
| 59 | Base directory for this skill: ${skillDir} |
| 60 |  |
| 61 | ${skill}`, |
| 62 | }, |
| 63 | ]; |
| 64 | }, |
| 65 | }, |
| 66 |  |
| 67 | execute: async (params, context) => { |
| 68 | const skillMarker = `[Skill: ${params.type}]`; |
| 69 |  |
| 70 | // Check if already loaded |
| 71 | if (JSON.stringify(context?.turnRequest?.input || []).includes(skillMarker)) { |
| 72 | return `Skill ${params.type} is already loaded`; |
| 73 | } |
| 74 |  |
| 75 | const skillPath = path.join(SKILLS_DIR, params.type, 'SKILL.md'); |
| 76 | if (!existsSync(skillPath)) { |
| 77 | const available = listAvailableSkills(); |
| 78 | return `Skill "${params.type}" not found. Available skills: ${available.join(', ') || 'none'}`; |
| 79 | } |
| 80 |  |
| 81 | return `Launching skill ${params.type}`; |
| 82 | }, |
| 83 | }); |
```

## Usage

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'anthropic/claude-sonnet-4.5', |
| 3 | input: 'I need to process a PDF and extract tables from it', |
| 4 | tools: [skillsTool], |
| 5 | }); |
| 6 |  |
| 7 | const text = await result.getText(); |
| 8 | // The model will call the Skill tool, loading pdf-processing context |
| 9 | // Subsequent responses will have access to the skill's instructions |
```

## Example Skill File

Create `~/.claude/skills/pdf-processing/SKILL.md`:

```
|  |  |
| --- | --- |
| 1 | # PDF Processing Skill |
| 2 |  |
| 3 | You are now equipped with PDF processing capabilities. |
| 4 |  |
| 5 | ## Available Tools |
| 6 | When processing PDFs, you have access to: |
| 7 | - `extract_text`: Extract all text from a PDF |
| 8 | - `extract_tables`: Extract tables as structured data |
| 9 | - `extract_images`: Extract embedded images |
| 10 | - `split_pdf`: Split PDF into individual pages |
| 11 |  |
| 12 | ## Best Practices |
| 13 | 1. Always check PDF file size before processing |
| 14 | 2. For large PDFs (>50 pages), process in chunks |
| 15 | 3. OCR may be needed for scanned documents |
| 16 | 4. Tables may span multiple pages - handle accordingly |
| 17 |  |
| 18 | ## Output Formats |
| 19 | - Text: Plain text or markdown |
| 20 | - Tables: JSON, CSV, or markdown tables |
| 21 | - Images: PNG with sequential naming |
| 22 |  |
| 23 | ## Error Handling |
| 24 | - If a PDF is encrypted, request the password |
| 25 | - If OCR fails, suggest alternative approaches |
| 26 | - Report page numbers for any extraction errors |
```

## Extended: Multi-Skill Loader

Load multiple skills in a single call:

```
|  |  |
| --- | --- |
| 1 | const multiSkillLoader = tool({ |
| 2 | name: 'load_skills', |
| 3 | description: 'Load multiple skills at once for complex tasks', |
| 4 |  |
| 5 | inputSchema: z.object({ |
| 6 | skills: z.array(z.string()).describe('Array of skill names to load'), |
| 7 | }), |
| 8 |  |
| 9 | outputSchema: z.object({ |
| 10 | loaded: z.array(z.string()), |
| 11 | failed: z.array( |
| 12 | z.object({ |
| 13 | name: z.string(), |
| 14 | reason: z.string(), |
| 15 | }) |
| 16 | ), |
| 17 | }), |
| 18 |  |
| 19 | nextTurnParams: { |
| 20 | input: (params, context) => { |
| 21 | let newInput = Array.isArray(context.input) ? context.input : [context.input]; |
| 22 |  |
| 23 | for (const skillName of params.skills) { |
| 24 | const skillMarker = `[Skill: ${skillName}]`; |
| 25 |  |
| 26 | // Skip if already loaded |
| 27 | if (JSON.stringify(newInput).includes(skillMarker)) { |
| 28 | continue; |
| 29 | } |
| 30 |  |
| 31 | const skillPath = path.join(SKILLS_DIR, skillName, 'SKILL.md'); |
| 32 | if (!existsSync(skillPath)) { |
| 33 | continue; |
| 34 | } |
| 35 |  |
| 36 | const skillContent = readFileSync(skillPath, 'utf-8'); |
| 37 | const skillDir = path.join(SKILLS_DIR, skillName); |
| 38 |  |
| 39 | newInput = [ |
| 40 | ...newInput, |
| 41 | { |
| 42 | role: 'user', |
| 43 | content: `${skillMarker} |
| 44 | Base directory: ${skillDir} |
| 45 |  |
| 46 | ${skillContent}`, |
| 47 | }, |
| 48 | ]; |
| 49 | } |
| 50 |  |
| 51 | return newInput; |
| 52 | }, |
| 53 | }, |
| 54 |  |
| 55 | execute: async ({ skills }) => { |
| 56 | const loaded: string[] = []; |
| 57 | const failed: Array<{ name: string; reason: string }> = []; |
| 58 |  |
| 59 | for (const skill of skills) { |
| 60 | const skillPath = path.join(SKILLS_DIR, skill, 'SKILL.md'); |
| 61 | if (existsSync(skillPath)) { |
| 62 | loaded.push(skill); |
| 63 | } else { |
| 64 | failed.push({ name: skill, reason: 'Skill not found' }); |
| 65 | } |
| 66 | } |
| 67 |  |
| 68 | return { loaded, failed }; |
| 69 | }, |
| 70 | }); |
| 71 |  |
| 72 | // Usage |
| 73 | const result = openrouter.callModel({ |
| 74 | model: 'anthropic/claude-sonnet-4.5', |
| 75 | input: 'I need to analyze a PDF report and create visualizations', |
| 76 | tools: [multiSkillLoader], |
| 77 | }); |
| 78 | // Model might call: load_skills({ skills: ['pdf-processing', 'data-analysis'] }) |
```

## Extended: Skill with Options

Skills that accept configuration:

```
|  |  |
| --- | --- |
| 1 | const configurableSkillLoader = tool({ |
| 2 | name: 'configure_skill', |
| 3 | description: 'Load a skill with custom configuration options', |
| 4 |  |
| 5 | inputSchema: z.object({ |
| 6 | skillName: z.string(), |
| 7 | options: z |
| 8 | .object({ |
| 9 | verbosity: z.enum(['minimal', 'normal', 'detailed']).default('normal'), |
| 10 | strictMode: z.boolean().default(false), |
| 11 | outputFormat: z.enum(['json', 'markdown', 'plain']).default('markdown'), |
| 12 | }) |
| 13 | .optional(), |
| 14 | }), |
| 15 |  |
| 16 | outputSchema: z.object({ |
| 17 | status: z.enum(['loaded', 'already_loaded', 'not_found']), |
| 18 | message: z.string(), |
| 19 | configuration: z.record(z.unknown()).optional(), |
| 20 | }), |
| 21 |  |
| 22 | nextTurnParams: { |
| 23 | input: (params, context) => { |
| 24 | const skillMarker = `[Skill: ${params.skillName}]`; |
| 25 | if (JSON.stringify(context.input).includes(skillMarker)) { |
| 26 | return context.input; |
| 27 | } |
| 28 |  |
| 29 | const skillPath = path.join(SKILLS_DIR, params.skillName, 'SKILL.md'); |
| 30 | if (!existsSync(skillPath)) { |
| 31 | return context.input; |
| 32 | } |
| 33 |  |
| 34 | const skillContent = readFileSync(skillPath, 'utf-8'); |
| 35 | const options = params.options || {}; |
| 36 |  |
| 37 | // Build configuration header |
| 38 | const configHeader = ` |
| 39 | ## Skill Configuration |
| 40 | - Verbosity: ${options.verbosity || 'normal'} |
| 41 | - Strict Mode: ${options.strictMode || false} |
| 42 | - Output Format: ${options.outputFormat || 'markdown'} |
| 43 | `; |
| 44 |  |
| 45 | const currentInput = Array.isArray(context.input) ? context.input : [context.input]; |
| 46 |  |
| 47 | return [ |
| 48 | ...currentInput, |
| 49 | { |
| 50 | role: 'user', |
| 51 | content: `${skillMarker} |
| 52 | ${configHeader} |
| 53 |  |
| 54 | ${skillContent}`, |
| 55 | }, |
| 56 | ]; |
| 57 | }, |
| 58 |  |
| 59 | // Adjust model behavior based on skill |
| 60 | temperature: (params, context) => { |
| 61 | // Lower temperature for strict mode |
| 62 | if (params.options?.strictMode) { |
| 63 | return 0.3; |
| 64 | } |
| 65 | return context.temperature; |
| 66 | }, |
| 67 | }, |
| 68 |  |
| 69 | execute: async ({ skillName, options }) => { |
| 70 | const skillPath = path.join(SKILLS_DIR, skillName, 'SKILL.md'); |
| 71 |  |
| 72 | if (!existsSync(skillPath)) { |
| 73 | return { |
| 74 | status: 'not_found' as const, |
| 75 | message: `Skill "${skillName}" not found`, |
| 76 | }; |
| 77 | } |
| 78 |  |
| 79 | return { |
| 80 | status: 'loaded' as const, |
| 81 | message: `Skill "${skillName}" loaded with configuration`, |
| 82 | configuration: options || {}, |
| 83 | }; |
| 84 | }, |
| 85 | }); |
```

## Skill Discovery Tool

List and describe available skills:

```
|  |  |
| --- | --- |
| 1 | const skillDiscoveryTool = tool({ |
| 2 | name: 'list_skills', |
| 3 | description: 'List all available skills with their descriptions', |
| 4 |  |
| 5 | inputSchema: z.object({ |
| 6 | category: z.string().optional().describe('Filter by category'), |
| 7 | }), |
| 8 |  |
| 9 | outputSchema: z.object({ |
| 10 | skills: z.array( |
| 11 | z.object({ |
| 12 | name: z.string(), |
| 13 | description: z.string(), |
| 14 | hasConfig: z.boolean(), |
| 15 | }) |
| 16 | ), |
| 17 | totalCount: z.number(), |
| 18 | }), |
| 19 |  |
| 20 | execute: async ({ category }) => { |
| 21 | const availableSkills = listAvailableSkills(); |
| 22 | const skills = []; |
| 23 |  |
| 24 | for (const skillName of availableSkills) { |
| 25 | const skillPath = path.join(SKILLS_DIR, skillName, 'SKILL.md'); |
| 26 | const content = readFileSync(skillPath, 'utf-8'); |
| 27 |  |
| 28 | // Extract first paragraph as description |
| 29 | const lines = content.split('\n').filter((l) => l.trim()); |
| 30 | const description = lines.find((l) => !l.startsWith('#')) || 'No description'; |
| 31 |  |
| 32 | // Check for config file |
| 33 | const configPath = path.join(SKILLS_DIR, skillName, 'config.json'); |
| 34 | const hasConfig = existsSync(configPath); |
| 35 |  |
| 36 | skills.push({ |
| 37 | name: skillName, |
| 38 | description: description.slice(0, 100), |
| 39 | hasConfig, |
| 40 | }); |
| 41 | } |
| 42 |  |
| 43 | return { |
| 44 | skills, |
| 45 | totalCount: skills.length, |
| 46 | }; |
| 47 | }, |
| 48 | }); |
```

## Complete Example

Putting it all together:

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter, tool, stepCountIs } from '@openrouter/agent'; |
| 2 | import { readFileSync, existsSync, readdirSync } from 'fs'; |
| 3 | import path from 'path'; |
| 4 | import { z } from 'zod'; |
| 5 |  |
| 6 | const openrouter = new OpenRouter({ |
| 7 | apiKey: process.env.OPENROUTER_API_KEY, |
| 8 | }); |
| 9 |  |
| 10 | const SKILLS_DIR = path.join(process.env.HOME || '~', '.claude', 'skills'); |
| 11 |  |
| 12 | // ... (include skillsTool, multiSkillLoader, skillDiscoveryTool from above) |
| 13 |  |
| 14 | // Use all skill tools together |
| 15 | const result = openrouter.callModel({ |
| 16 | model: 'anthropic/claude-sonnet-4.5', |
| 17 | input: `I have a complex task: |
| 18 | 1. First, show me what skills are available |
| 19 | 2. Load the appropriate skills for PDF analysis |
| 20 | 3. Then help me extract and analyze data from report.pdf`, |
| 21 | tools: [skillDiscoveryTool, skillsTool, multiSkillLoader], |
| 22 | stopWhen: stepCountIs(10), |
| 23 | }); |
| 24 |  |
| 25 | const text = await result.getText(); |
| 26 | console.log(text); |
```

## Key Patterns

### 1. Idempotency

Always check if a skill is already loaded:

```
|  |  |
| --- | --- |
| 1 | nextTurnParams: { |
| 2 | input: (params, context) => { |
| 3 | const marker = `[Skill: ${params.type}]`; |
| 4 | if (JSON.stringify(context.input).includes(marker)) { |
| 5 | return context.input; // Don't add again |
| 6 | } |
| 7 | // ... add skill |
| 8 | }, |
| 9 | }, |
```

### 2. Graceful Fallbacks

Handle missing skills gracefully:

```
|  |  |
| --- | --- |
| 1 | execute: async (params) => { |
| 2 | if (!existsSync(skillPath)) { |
| 3 | return `Skill not found. Available: ${listAvailableSkills().join(', ')}`; |
| 4 | } |
| 5 | // ... |
| 6 | }, |
```

### 3. Context Preservation

Always preserve existing input:

```
|  |  |
| --- | --- |
| 1 | nextTurnParams: { |
| 2 | input: (params, context) => { |
| 3 | const currentInput = Array.isArray(context.input) |
| 4 | ? context.input |
| 5 | : [context.input]; |
| 6 | return [...currentInput, newMessage]; // Append, don't replace |
| 7 | }, |
| 8 | }, |
```

### 4. Clear Markers

Use unique markers to identify injected content:

```
|  |  |
| --- | --- |
| 1 | const skillMarker = `[Skill: ${params.type}]`; |
| 2 | // Makes detection reliable and content clearly labeled |
```

## See Also

- **[nextTurnParams Guide](../../../../call-model/next-turn-params/index.md)** - Context injection patterns
- **[Dynamic Parameters](../../../../call-model/dynamic-parameters/index.md)** - Adaptive behavior
- **[Tools](../../../../call-model/tools/index.md)** - Multi-turn orchestration
