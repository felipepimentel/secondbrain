FROM python:3.12.5-slim-bookworm AS python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Fase de construção (builder-base)
FROM python-base AS builder-base
RUN apt-get update && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        tesseract-ocr && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.3
RUN curl -sSL https://install.python-poetry.org | python

WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --no-root --no-dev

# Fase de desenvolvimento
FROM builder-base AS development

WORKDIR /app
COPY . .

RUN poetry install

CMD ["python", "-m", "myapplication.main"]

# Fase de produção
FROM python-base AS production

WORKDIR /app

# Copiar apenas as dependências essenciais da fase builder-base
COPY --from=builder-base $VENV_PATH $VENV_PATH
COPY ./src/ ./

USER 10000

CMD ["python", "-m", "myapplication.main"]
