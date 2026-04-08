---
source_url: "https://openrouter.ai/docs/guides/features/broadcast/clickhouse"
title: "Broadcast to ClickHouse | OpenRouter Observability | OpenRouter | Documentation"
crawled_at: "2026-04-08T10:29:36.196215+00:00"
---
[Features](../../presets/index.md)[Broadcast](../overview/index.md)

# ClickHouse

Send traces to ClickHouse

[ClickHouse](https://clickhouse.com/) is a fast, open-source columnar database for real-time analytics. OpenRouter can stream traces directly to your ClickHouse database for high-performance analytics and custom dashboards.

## Step 1: Create the traces table

Before connecting OpenRouter, create the `OPENROUTER_TRACES` table in your ClickHouse database. You can find the exact SQL in the OpenRouter dashboard when configuring the destination:

![ClickHouse Setup Instructions](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/5c24c1cafb5b6b4fade072d9624cb8f997a997de69f01dbe26e097d90938f488/content/pages/features/broadcast/broadcast-clickhouse-setup.png)

## Step 2: Set up permissions

Ensure your ClickHouse user has CREATE TABLE permissions:

```
|  |  |
| --- | --- |
| 1 | GRANT CREATE TABLE ON your_database.* TO your_database_user; |
```

## Step 3: Enable Broadcast in OpenRouter

Go to [Settings > Observability](https://openrouter.ai/settings/observability) and toggle **Enable Broadcast**.

![Enable Broadcast](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/3e095d95758bab05594f468011be81b7d5a2fb19293fa91d5b3923d9f09b81d8/content/pages/features/broadcast/broadcast-enable.png)

## Step 4: Configure ClickHouse

Click the edit icon next to **ClickHouse** and enter:

![ClickHouse Configuration](https://files.buildwithfern.com/openrouter.docs.buildwithfern.com/docs/7cb1f2b37ea07e292bcce47af9c7667b44e4fa45becf4795e0d73ac0d98da03f/content/pages/features/broadcast/broadcast-clickhouse-config.png)

- **Host**: Your ClickHouse HTTP endpoint (e.g., `https://clickhouse.example.com:8123`)
- **Database**: Target database name (default: `default`)
- **Table**: Table name (default: `OPENROUTER_TRACES`)
- **Username**: ClickHouse username for authentication (defaults to `default`)
- **Password**: ClickHouse password for authentication

##### 

For ClickHouse Cloud, your host URL is typically `https://{instance}.{region}.clickhouse.cloud:8443`. You can find this in your ClickHouse Cloud console [under **Connect**](https://clickhouse.com/docs/cloud/guides/sql-console/gather-connection-details).

## Step 5: Test and save

Click **Test Connection** to verify the setup. The configuration only saves if the test passes.

## Step 6: Send a test trace

Make an API request through OpenRouter and query your ClickHouse table to verify the trace was received.

## Example queries

### Cost analysis by model

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | toDate(TIMESTAMP) as day, |
| 3 | MODEL, |
| 4 | sum(TOTAL_COST) as total_cost, |
| 5 | sum(TOTAL_TOKENS) as total_tokens, |
| 6 | count() as request_count |
| 7 | FROM OPENROUTER_TRACES |
| 8 | WHERE TIMESTAMP >= now() - INTERVAL 30 DAY |
| 9 | AND STATUS = 'ok' |
| 10 | AND SPAN_TYPE = 'GENERATION' |
| 11 | GROUP BY day, MODEL |
| 12 | ORDER BY day DESC, total_cost DESC; |
```

### User activity analysis

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | USER_ID, |
| 3 | uniqExact(TRACE_ID) as trace_count, |
| 4 | uniqExact(SESSION_ID) as session_count, |
| 5 | sum(TOTAL_TOKENS) as total_tokens, |
| 6 | sum(TOTAL_COST) as total_cost, |
| 7 | avg(DURATION_MS) as avg_duration_ms |
| 8 | FROM OPENROUTER_TRACES |
| 9 | WHERE TIMESTAMP >= now() - INTERVAL 7 DAY |
| 10 | AND SPAN_TYPE = 'GENERATION' |
| 11 | GROUP BY USER_ID |
| 12 | ORDER BY total_cost DESC; |
```

### Error analysis

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | TRACE_ID, |
| 3 | TIMESTAMP, |
| 4 | MODEL, |
| 5 | LEVEL, |
| 6 | FINISH_REASON, |
| 7 | METADATA, |
| 8 | INPUT, |
| 9 | OUTPUT |
| 10 | FROM OPENROUTER_TRACES |
| 11 | WHERE STATUS = 'error' |
| 12 | AND TIMESTAMP >= now() - INTERVAL 1 HOUR |
| 13 | ORDER BY TIMESTAMP DESC; |
```

### Provider performance comparison

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | PROVIDER_NAME, |
| 3 | MODEL, |
| 4 | avg(DURATION_MS) as avg_duration_ms, |
| 5 | quantile(0.5)(DURATION_MS) as p50_duration_ms, |
| 6 | quantile(0.95)(DURATION_MS) as p95_duration_ms, |
| 7 | count() as request_count |
| 8 | FROM OPENROUTER_TRACES |
| 9 | WHERE TIMESTAMP >= now() - INTERVAL 7 DAY |
| 10 | AND STATUS = 'ok' |
| 11 | AND SPAN_TYPE = 'GENERATION' |
| 12 | GROUP BY PROVIDER_NAME, MODEL |
| 13 | HAVING request_count >= 10 |
| 14 | ORDER BY avg_duration_ms; |
```

### Usage by API key

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | API_KEY_NAME, |
| 3 | uniqExact(TRACE_ID) as trace_count, |
| 4 | sum(TOTAL_COST) as total_cost, |
| 5 | sum(PROMPT_TOKENS) as prompt_tokens, |
| 6 | sum(COMPLETION_TOKENS) as completion_tokens |
| 7 | FROM OPENROUTER_TRACES |
| 8 | WHERE TIMESTAMP >= now() - INTERVAL 30 DAY |
| 9 | AND SPAN_TYPE = 'GENERATION' |
| 10 | GROUP BY API_KEY_NAME |
| 11 | ORDER BY total_cost DESC; |
```

### Accessing JSON columns

ClickHouse stores JSON data as strings. Use `JSONExtract` functions to query
nested fields:

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | TRACE_ID, |
| 3 | JSONExtractString(METADATA, 'custom_field') as custom_value, |
| 4 | JSONExtractString(ATTRIBUTES, 'gen_ai.request.model') as requested_model |
| 5 | FROM OPENROUTER_TRACES |
| 6 | WHERE JSONHas(METADATA, 'custom_field'); |
```

To parse input messages:

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | TRACE_ID, |
| 3 | JSONExtractString( |
| 4 | JSONExtractRaw(INPUT, 'messages'), |
| 5 | 1, 'role' |
| 6 | ) as first_message_role, |
| 7 | JSONExtractString( |
| 8 | JSONExtractRaw(INPUT, 'messages'), |
| 9 | 1, 'content' |
| 10 | ) as first_message_content |
| 11 | FROM OPENROUTER_TRACES |
| 12 | WHERE SPAN_TYPE = 'GENERATION' |
| 13 | LIMIT 10; |
```

## Schema design

### Typed columns

The schema extracts commonly-queried fields as typed columns for efficient filtering and aggregation:

- **Identifiers**: TRACE\_ID, USER\_ID, SESSION\_ID, etc.
- **Timestamps**: DateTime64 for time-series analysis with millisecond precision
- **Model Info**: For cost and performance analysis
- **Metrics**: Tokens and costs for billing

### String columns for JSON

Less commonly-accessed and variable-structure data is stored as JSON strings:

- **ATTRIBUTES**: Full OTEL attribute set
- **INPUT/OUTPUT**: Variable message structures
- **METADATA**: User-defined key-values
- **MODEL\_PARAMETERS**: Model-specific configurations

Use ClickHouse’s `JSONExtract*` functions to query these fields.

## Custom Metadata

Custom metadata from the `trace` field is stored in the `METADATA` column as a JSON string. You can query it using ClickHouse’s `JSONExtract` functions.

### Supported Metadata Keys

| Key | ClickHouse Mapping | Description |
| --- | --- | --- |
| `trace_id` | `TRACE_ID` column / `METADATA` JSON | Custom trace identifier for grouping |
| `trace_name` | `METADATA` JSON | Custom name for the trace |
| `span_name` | `METADATA` JSON | Name for intermediate spans |
| `generation_name` | `METADATA` JSON | Name for the LLM generation |

### Example

```
|  |  |
| --- | --- |
| 1 | { |
| 2 | "model": "openai/gpt-4o", |
| 3 | "messages": [{ "role": "user", "content": "Analyze these metrics..." }], |
| 4 | "user": "user_12345", |
| 5 | "session_id": "session_abc", |
| 6 | "trace": { |
| 7 | "trace_name": "Metrics Analysis Pipeline", |
| 8 | "generation_name": "Analyze Trends", |
| 9 | "team": "data-engineering", |
| 10 | "pipeline_version": "2.0", |
| 11 | "data_source": "clickhouse_metrics" |
| 12 | } |
| 13 | } |
```

### Querying Custom Metadata

Use ClickHouse’s JSON functions to query your custom metadata:

```
|  |  |
| --- | --- |
| 1 | SELECT |
| 2 | TRACE_ID, |
| 3 | JSONExtractString(METADATA, 'team') as team, |
| 4 | JSONExtractString(METADATA, 'pipeline_version') as pipeline_version, |
| 5 | JSONExtractString(METADATA, 'data_source') as data_source, |
| 6 | TOTAL_COST, |
| 7 | TOTAL_TOKENS |
| 8 | FROM OPENROUTER_TRACES |
| 9 | WHERE JSONHas(METADATA, 'team') |
| 10 | AND SPAN_TYPE = 'GENERATION' |
| 11 | ORDER BY TIMESTAMP DESC; |
```

### Additional Context

- The `user` field maps to the `USER_ID` typed column
- The `session_id` field maps to the `SESSION_ID` typed column
- All custom metadata keys from `trace` are stored in the `METADATA` JSON string column
- For high-performance filtering on metadata fields, consider creating materialized columns with `ALTER TABLE ... ADD COLUMN`

## Additional resources

- [ClickHouse HTTP Interface Documentation](https://clickhouse.com/docs/en/interfaces/http)
- [ClickHouse SQL Reference](https://clickhouse.com/docs/en/sql-reference)
- [ClickHouse Cloud](https://clickhouse.com/cloud)

## Privacy Mode

When [Privacy Mode](../index.md) is enabled for this destination, prompt and completion content is excluded from traces. All other trace data — token usage, costs, timing, model information, and custom metadata — is still sent normally. See [Privacy Mode](../index.md) for details.
