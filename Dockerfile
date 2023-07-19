FROM python:3.10 as build_app


WORKDIR /app

ENV PYTHONBUFFERED 1\
    PYTHONDONTWRITEBYTECODE 1

COPY poetry.lock pyproject.toml ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false

EXPOSE 8001

COPY . /app

FROM build_app as development

RUN poetry install --with dev

CMD alembic upgrade head && python -m src