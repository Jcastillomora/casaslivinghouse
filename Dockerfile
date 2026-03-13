# Stage 1: init
FROM python:3.13 as init

ARG uv=/root/.local/bin/uv

# Install `uv` for faster package bootstrapping
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

WORKDIR /app
COPY . .
RUN mkdir -p /app/data

# Create virtualenv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN $uv venv

# Install dependencies
RUN $uv pip install -r requirements.txt

# Initialize and build frontend
RUN reflex init
RUN reflex export --frontend-only --no-zip

# Move static files out to slim down the backend image
RUN mv .web/build/client /tmp/client
RUN rm -rf .web && mkdir -p .web/build
RUN mv /tmp/client .web/build/client

# Stage 2: slim runtime image
FROM python:3.13-slim
WORKDIR /app
RUN adduser --disabled-password --home /app reflex
COPY --chown=reflex --from=init /app /app
USER reflex
ENV PATH="/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1

STOPSIGNAL SIGKILL

CMD exec reflex run --env prod --backend-only
