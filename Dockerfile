FROM python3.10-slim as build_app


WORKDIR /app

ENV PYTHONBUFFERED 1\
    PYTHONDONTWRITEBYTECODE 1\
COPY poetry.lock pyproject.toml ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false

COPY ./src /app

FROM build_app as development

RUN poetry isntall --with dev



FROM build_app as production

RUN poetry install --without dev