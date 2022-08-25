FROM python:3.10.6-slim-buster
ENV PYTHONBUFFERED 1

WORKDIR /home/alpha
ENV PYTHONPATH=${PYTHONPATH}/home/alpha
ADD pyproject.toml poetry.lock /home/alpha/

RUN apt update
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi
