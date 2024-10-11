FROM python:3.11-alpine

ENV PYTHONONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache \
    mariadb-dev \
    gcc \
    musl-dev \
    pkgconfig \
    build-base \
    bash

WORKDIR /app

COPY ["riverdata", "robeForecast", "staticfiles", "celerybeat_schedule.*", "manage.py", "requirements.txt", "start.sh", "wsgi.py", "/app/"]

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["./start.sh"]
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
