FROM python:3.10.4-slim-buster

WORKDIR /app

LABEL maintainer="vickadiata@gmail.com"
LABEL description="Development image for the Hospital GeoDjango API"

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev libpq-dev gdal-bin python-gdal python3-gdal

RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app
