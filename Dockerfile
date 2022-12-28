FROM python:3.9
LABEL maintainer='Brenim'

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"

USER django-user
# EXPOSE 8000