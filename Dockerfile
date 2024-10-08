FROM python:3.11-alpine

ENV PYTHONONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache \
    mariadb-dev \
    gcc \
    musl-dev \
    pkgconfig \
    build-base

WORKDIR /app

COPY requirements.txt /app/
#COPY start.sh /app/start.sh
#RUN chmod +x /app/start.sh
RUN #apk add --no-cache build-base gcc
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENTRYPOINT ["./start.sh"]
