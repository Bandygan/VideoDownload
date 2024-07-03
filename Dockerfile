FROM python:3.11-slim-buster

ADD . /application/
WORKDIR /application

ENV DJANGO_SETTINGS_MODULE jwt_project.settings

RUN pip3 install --no-cache-dir -r /application/requirements.txt