FROM python:3.10-slim

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG APP_USER=starterapi

ENV POETRY_VERSION=1.5.0 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_CREATE=false \
    #app
    APP_HOME="/usr/src/app" \
    VENV_PATH="/usr/src/app/.venv"

RUN apt-get update &&  \
    apt-get install -y \
    netcat-traditional \
    curl \
    postgresql \
    gcc \
    python3-dev \
    python3-pytest \
    libc6 \
    gnupg

RUN mkdir -p ${APP_HOME} ${POETRY_HOME} ${VENV_PATH} && \
    useradd -m -u 8888 --no-log-init ${APP_USER} && \
    chown -R ${APP_USER}:${APP_USER} ${POETRY_HOME} ${APP_HOME}

# SWITCH TO NON ROOT
USER ${APP_USER}
WORKDIR /usr/src/app

# INSTALL POETRY
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${POETRY_HOME}/bin:${VENV_PATH}/bin:${PATH}"

# INSTALL POETRY DEPENDENCIES
COPY --chown=$APP_USER:$APP_USER ./backend/poetry.lock ./backend/pyproject.toml ./
RUN poetry install --no-root --no-interaction --no-ansi

COPY ./backend /usr/src/app

