# syntax=docker/dockerfile:1

FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python -m spacy download en
#RUN apt-get install -y sqlite3 libsqlite3-dev

COPY . .

ENV FLASK_APP=web_app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
