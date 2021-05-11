FROM python:3.8-slim-buster

RUN  apt-get -y update
RUN apt-get -y upgrade

WORKDIR /ETL

ADD . /ETL
ENV FLASK_APP app.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet
RUN python3 -m nltk.downloader words
RUN chmod u+x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
