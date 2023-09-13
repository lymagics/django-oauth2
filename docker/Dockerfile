FROM python:slim

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY authy authy
COPY waitlist waitlist
WORKDIR /authy