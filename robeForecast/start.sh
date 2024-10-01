#!/bin/bash

python manage.py migrate
python manage.py collectstatic --noinput

celery -A robeForecast worker --loglevel=INFO --concurrency 1 -P solo &
celery -A robeForecast beat --loglevel=INFO &

gunicorn robeForecast.wsgi:application --bind 0.0.0.0:8000
