FROM node:26-bookworm-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PORT=3000 \
    HOST=0.0.0.0 \
    PYTHON_PATH=/opt/venv/bin/python \
    FASTEMBED_CACHE_PATH=/app/.cache/fastembed

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-venv \
    ca-certificates \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/day26-ai-cloud-support-assistant

COPY day26-ai-cloud-support-assistant/package.json \
     day26-ai-cloud-support-assistant/package-lock.json ./

RUN npm ci --omit=dev

RUN python3 -m venv /opt/venv

COPY day26-ai-cloud-support-assistant/requirements.txt /tmp/requirements.txt

RUN /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install -r /tmp/requirements.txt

COPY day26-ai-cloud-support-assistant/src ./src
COPY day26-ai-cloud-support-assistant/public ./public

COPY day25-rag-pipeline /app/day25-rag-pipeline
COPY day24-embeddings-retrieval/lab2-chunking/chunks \
     /app/day24-embeddings-retrieval/lab2-chunking/chunks

RUN mkdir -p /app/.cache/fastembed \
    && chown -R node:node /app

USER node

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD node -e "fetch('http://127.0.0.1:3000/health').then(r => process.exit(r.ok ? 0 : 1)).catch(() => process.exit(1))"

CMD ["npm", "start"]
