FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY . .

ENV PORT=8000
ENV DOC_GETTER_DATA_DIR=/tmp/doc-getter-runs

EXPOSE 8000

CMD ["uv", "run", "python", "service.py"]
