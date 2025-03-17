FROM python:3.13

WORKDIR /opt/gebieden-api-client

# Install Poetry
RUN set eux; \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python; \
    cd /usr/local/bin; \
    ln -s /opt/poetry/bin/poetry; \
    poetry config virtualenvs.create false; \
    poetry self add poetry-plugin-sort

COPY ./pyproject.toml ./poetry.lock /opt/gebieden-api-client/

RUN poetry install --no-root
ENV PYTHONPATH=/opt/gebieden-api-client
