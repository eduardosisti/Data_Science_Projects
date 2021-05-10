FROM python:3.8-slim

WORKDIR /ETL

ADD . /ETL

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet
RUN python3 -m nltk.downloader words

CMD ["python", "./manage.py"]