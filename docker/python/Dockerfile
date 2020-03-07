FROM python:3.7-alpine

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV TERM screen
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app