FROM python:3.10
LABEL maintainer="Fraxize"

COPY ./requirements.txt  /app/
COPY ./web_app  /app/

WORKDIR /app/

RUN pip install -r requirements.txt
CMD python ./web_app.py
