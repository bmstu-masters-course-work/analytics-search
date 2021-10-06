# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /project
COPY /project/requirements.txt /project/
RUN pip install -r requirements.txt
COPY . /project/