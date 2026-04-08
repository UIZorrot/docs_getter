---
source_url: "https://openrouter.ai/docs/sdks/typescript/call-model/examples/weather-tool"
title: "Weather Tool Example | OpenRouter SDK | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:48.346936+00:00"
---
[TypeScript SDK](../../../overview/index.md)[Call Model](../../overview/index.md)[Examples](index.md)

# Weather Tool

A complete weather tool demonstrating external API integration, proper validation, and error handling.

## Prerequisites

```
|  |  |
| --- | --- |
| $ | pnpm add @openrouter/sdk zod |
```

You’ll need a weather API key. This example uses [WeatherAPI](https://www.weatherapi.com/) (free tier available).

```
|  |  |
| --- | --- |
| $ | export WEATHER_API_KEY=your_api_key_here |
| $ | export OPENROUTER_API_KEY=your_openrouter_key |
```

## Basic Implementation

```
|  |  |
| --- | --- |
| 1 | import { OpenRouter, tool } from '@openrouter/agent'; |
| 2 | import { z } from 'zod'; |
| 3 |  |
| 4 | const openrouter = new OpenRouter({ |
| 5 | apiKey: process.env.OPENROUTER_API_KEY, |
| 6 | }); |
| 7 |  |
| 8 | const weatherTool = tool({ |
| 9 | name: 'get_weather', |
| 10 | description: 'Get current weather conditions for any city worldwide', |
| 11 | inputSchema: z.object({ |
| 12 | city: z.string().describe('City name, e.g., "San Francisco" or "London, UK"'), |
| 13 | units: z |
| 14 | .enum(['celsius', 'fahrenheit']) |
| 15 | .default('celsius') |
| 16 | .describe('Temperature units'), |
| 17 | }), |
| 18 | outputSchema: z.object({ |
| 19 | temperature: z.number(), |
| 20 | feelsLike: z.number(), |
| 21 | conditions: z.string(), |
| 22 | humidity: z.number(), |
| 23 | windSpeed: z.number(), |
| 24 | windDirection: z.string(), |
| 25 | location: z.object({ |
| 26 | name: z.string(), |
| 27 | region: z.string(), |
| 28 | country: z.string(), |
| 29 | }), |
| 30 | }), |
| 31 | execute: async ({ city, units }) => { |
| 32 | const apiKey = process.env.WEATHER_API_KEY; |
| 33 | if (!apiKey) { |
| 34 | throw new Error('WEATHER_API_KEY environment variable not set'); |
| 35 | } |
| 36 |  |
| 37 | const response = await fetch( |
| 38 | `https://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${encodeURIComponent(city)}` |
| 39 | ); |
| 40 |  |
| 41 | if (!response.ok) { |
| 42 | if (response.status === 400) { |
| 43 | throw new Error(`City not found: ${city}`); |
| 44 | } |
| 45 | throw new Error(`Weather API error: ${response.status}`); |
| 46 | } |
| 47 |  |
| 48 | const data = await response.json(); |
| 49 |  |
| 50 | return { |
| 51 | temperature: units === 'celsius' ? data.current.temp_c : data.current.temp_f, |
| 52 | feelsLike: units === 'celsius' ? data.current.feelslike_c : data.current.feelslike_f, |
| 53 | conditions: data.current.condition.text, |
| 54 | humidity: data.current.humidity, |
| 55 | windSpeed: data.current.wind_kph, |
| 56 | windDirection: data.current.wind_dir, |
| 57 | location: { |
| 58 | name: data.location.name, |
| 59 | region: data.location.region, |
| 60 | country: data.location.country, |
| 61 | }, |
| 62 | }; |
| 63 | }, |
| 64 | }); |
```

## Usage

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'What is the weather like in Tokyo?', |
| 4 | tools: [weatherTool], |
| 5 | }); |
| 6 |  |
| 7 | const text = await result.getText(); |
| 8 | console.log(text); |
| 9 | // "The current weather in Tokyo, Japan is partly cloudy with a temperature |
| 10 | // of 22°C (feels like 24°C). Humidity is at 65% with winds from the SW |
| 11 | // at 15 km/h." |
```

## With Multiple Cities

```
|  |  |
| --- | --- |
| 1 | const result = openrouter.callModel({ |
| 2 | model: 'openai/gpt-5-nano', |
| 3 | input: 'Compare the weather in New York and Los Angeles', |
| 4 | tools: [weatherTool], |
| 5 | }); |
| 6 |  |
| 7 | // The model will call the tool twice, once for each city |
| 8 | const text = await result.getText(); |
```

## Extended Version with Forecast

```
|  |  |
| --- | --- |
| 1 | const forecastTool = tool({ |
| 2 | name: 'get_forecast', |
| 3 | description: 'Get weather forecast for the next few days', |
| 4 | inputSchema: z.object({ |
| 5 | city: z.string().describe('City name'), |
| 6 | days: z.number().min(1).max(7).default(3).describe('Number of forecast days'), |
| 7 | units: z.enum(['celsius', 'fahrenheit']).default('celsius'), |
| 8 | }), |
| 9 | outputSchema: z.object({ |
| 10 | location: z.string(), |
| 11 | forecast: z.array( |
| 12 | z.object({ |
| 13 | date: z.string(), |
| 14 | maxTemp: z.number(), |
| 15 | minTemp: z.number(), |
| 16 | conditions: z.string(), |
| 17 | chanceOfRain: z.number(), |
| 18 | }) |
| 19 | ), |
| 20 | }), |
| 21 | execute: async ({ city, days, units }) => { |
| 22 | const apiKey = process.env.WEATHER_API_KEY; |
| 23 | if (!apiKey) { |
| 24 | throw new Error('WEATHER_API_KEY environment variable not set'); |
| 25 | } |
| 26 |  |
| 27 | const response = await fetch( |
| 28 | `https://api.weatherapi.com/v1/forecast.json?key=${apiKey}&q=${encodeURIComponent(city)}&days=${days}` |
| 29 | ); |
| 30 |  |
| 31 | if (!response.ok) { |
| 32 | throw new Error(`Weather API error: ${response.status}`); |
| 33 | } |
| 34 |  |
| 35 | const data = await response.json(); |
| 36 |  |
| 37 | return { |
| 38 | location: `${data.location.name}, ${data.location.country}`, |
| 39 | forecast: data.forecast.forecastday.map((day: any) => ({ |
| 40 | date: day.date, |
| 41 | maxTemp: units === 'celsius' ? day.day.maxtemp_c : day.day.maxtemp_f, |
| 42 | minTemp: units === 'celsius' ? day.day.mintemp_c : day.day.mintemp_f, |
| 43 | conditions: day.day.condition.text, |
| 44 | chanceOfRain: day.day.daily_chance_of_rain, |
| 45 | })), |
| 46 | }; |
| 47 | }, |
| 48 | }); |
| 49 |  |
| 50 | // Use both tools together |
| 51 | const result = openrouter.callModel({ |
| 52 | model: 'openai/gpt-5-nano', |
| 53 | input: 'What is the weather in Paris today and for the next 3 days?', |
| 54 | tools: [weatherTool, forecastTool], |
| 55 | }); |
```

## Error Handling

The tool includes proper error handling:

```
|  |  |
| --- | --- |
| 1 | const weatherToolWithRetry = tool({ |
| 2 | name: 'get_weather', |
| 3 | description: 'Get current weather with retry logic', |
| 4 | inputSchema: z.object({ |
| 5 | city: z.string(), |
| 6 | units: z.enum(['celsius', 'fahrenheit']).default('celsius'), |
| 7 | }), |
| 8 | outputSchema: z.object({ |
| 9 | temperature: z.number(), |
| 10 | conditions: z.string(), |
| 11 | error: z.string().optional(), |
| 12 | }), |
| 13 | execute: async ({ city, units }) => { |
| 14 | const maxRetries = 3; |
| 15 | let lastError: Error | null = null; |
| 16 |  |
| 17 | for (let attempt = 1; attempt <= maxRetries; attempt++) { |
| 18 | try { |
| 19 | const response = await fetch( |
| 20 | `https://api.weatherapi.com/v1/current.json?key=${process.env.WEATHER_API_KEY}&q=${encodeURIComponent(city)}` |
| 21 | ); |
| 22 |  |
| 23 | if (response.status === 429) { |
| 24 | // Rate limited, wait and retry |
| 25 | await new Promise((resolve) => setTimeout(resolve, 1000 * attempt)); |
| 26 | continue; |
| 27 | } |
| 28 |  |
| 29 | if (!response.ok) { |
| 30 | throw new Error(`API error: ${response.status}`); |
| 31 | } |
| 32 |  |
| 33 | const data = await response.json(); |
| 34 | return { |
| 35 | temperature: units === 'celsius' ? data.current.temp_c : data.current.temp_f, |
| 36 | conditions: data.current.condition.text, |
| 37 | }; |
| 38 | } catch (error) { |
| 39 | lastError = error as Error; |
| 40 | } |
| 41 | } |
| 42 |  |
| 43 | // Return error in output rather than throwing |
| 44 | return { |
| 45 | temperature: 0, |
| 46 | conditions: 'Unknown', |
| 47 | error: `Failed after ${maxRetries} attempts: ${lastError?.message}`, |
| 48 | }; |
| 49 | }, |
| 50 | }); |
```

## Testing

```
|  |  |
| --- | --- |
| 1 | import { describe, it, expect, mock } from 'bun:test'; |
| 2 |  |
| 3 | describe('weatherTool', () => { |
| 4 | it('returns weather data for valid city', async () => { |
| 5 | // Mock the fetch response |
| 6 | global.fetch = mock(() => |
| 7 | Promise.resolve({ |
| 8 | ok: true, |
| 9 | json: () => |
| 10 | Promise.resolve({ |
| 11 | current: { |
| 12 | temp_c: 22, |
| 13 | temp_f: 72, |
| 14 | feelslike_c: 24, |
| 15 | feelslike_f: 75, |
| 16 | condition: { text: 'Sunny' }, |
| 17 | humidity: 45, |
| 18 | wind_kph: 10, |
| 19 | wind_dir: 'NW', |
| 20 | }, |
| 21 | location: { |
| 22 | name: 'London', |
| 23 | region: 'City of London', |
| 24 | country: 'UK', |
| 25 | }, |
| 26 | }), |
| 27 | }) |
| 28 | ); |
| 29 |  |
| 30 | const result = await weatherTool.function.execute( |
| 31 | { city: 'London', units: 'celsius' }, |
| 32 | { numberOfTurns: 1 } |
| 33 | ); |
| 34 |  |
| 35 | expect(result.temperature).toBe(22); |
| 36 | expect(result.conditions).toBe('Sunny'); |
| 37 | expect(result.location.name).toBe('London'); |
| 38 | }); |
| 39 |  |
| 40 | it('handles city not found', async () => { |
| 41 | global.fetch = mock(() => |
| 42 | Promise.resolve({ |
| 43 | ok: false, |
| 44 | status: 400, |
| 45 | }) |
| 46 | ); |
| 47 |  |
| 48 | await expect( |
| 49 | weatherTool.function.execute( |
| 50 | { city: 'InvalidCity123', units: 'celsius' }, |
| 51 | { numberOfTurns: 1 } |
| 52 | ) |
| 53 | ).rejects.toThrow('City not found'); |
| 54 | }); |
| 55 | }); |
```

## See Also

- **[Tools Guide](../../../../call-model/tools/index.md)** - Tool creation fundamentals
- **[API Reference](../../../../call-model/api-reference/index.md)** - Complete type definitions
