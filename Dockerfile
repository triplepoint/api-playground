FROM python:3.14 AS base

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

WORKDIR /app

COPY ./ ./

RUN /root/.local/bin/uv sync

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["/root/.local/bin/uv", "run", "fastapi", "run", "main.py", "--proxy-headers", "--port", "80", "--reload"]
