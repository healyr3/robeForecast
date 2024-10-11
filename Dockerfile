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

#ENTRYPOINT ["./start.sh"]

CMD ["sh", "-c", "until ping -c 1 robeforecast-mysql &> /dev/null; do echo 'Waiting for database...'; sleep 5; done"]
CMD ["python", "manage.py", "collectstatic", "--noinput"]
CMD ["celery", "-A", "robeForecast", "worker", "--loglevel=INFO", "--concurrency", "1", "-P", "solo", "&"]
CMD ["celery", "-A", "robeForecast", "beat", "--loglevel=INFO", "&"]
CMD ["gunicorn", "robeForecast.wsgi:application", "--bind", "0.0.0.0:8000"]
