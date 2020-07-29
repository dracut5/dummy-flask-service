FROM python:3.7.4-alpine3.10

RUN apk add --no-cache curl netcat-openbsd bash && pip install --no-cache-dir flask
RUN mkdir /app

COPY entrypoint.sh /entrypoint.sh

COPY main.py /app/main.py
COPY migration.sh /app/docker/provision/migration.sh
COPY files /app/files

RUN chmod 755 /app/main.py /entrypoint.sh /app/docker/provision/migration.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/app/main.py"]
