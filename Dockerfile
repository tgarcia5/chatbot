# syntax=docker/dockerfile:1

FROM python:3.7-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install -y git
RUN git clone https://github.com/gunthercox/ChatterBot.git
RUN pip install ./ChatterBot

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python -m spacy download en


COPY . .

ENV FLASK_APP=web_app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
