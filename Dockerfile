FROM python:3.9-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD ./src/app/ /app
WORKDIR /app

RUN apt-get update
RUN apt-get install build-essential libpq-dev -y

RUN pip install -r requirements.txt
