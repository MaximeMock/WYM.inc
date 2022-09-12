FROM python3.10.4
LABEL maintainer="Fraxize"

COPY ./requirements.txt app  /app/
COPY ./web_app  /app/

WORKDIR /app/

RUN pip install -r requirements.txt
CMD python ./web_app/.py
