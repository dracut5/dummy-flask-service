FROM python:3.7.4-alpine3.10

RUN apk add --no-cache curl netcat-openbsd && pip install --no-cache-dir flask

COPY main.py /main.py

RUN chmod 755 /main.py

ENTRYPOINT ["/main.py"]
