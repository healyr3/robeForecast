#!/bin/bash

echo "Starting Script"

echo "Waiting 5 seconds....."
sleep 5;

echo "Waiting 5 seconds....."
sleep 5;

echo "Waiting 5 seconds....."
sleep 5;

#until nc -z db 3306; do
#  echo "Waiting for database...";
#  sleep 5;
#done

#python manage.py makemigrations
#echo "Starting makemigrations"
#
#python manage.py migrate
#echo "Starting migrate"

python manage.py collectstatic --noinput
echo "Starting collectstatic"

celery -A robeForecast worker --loglevel=INFO --concurrency 1 -P solo &
echo "Starting celery worker"

celery -A robeForecast beat --loglevel=INFO &
echo "Starting celery beat"

gunicorn robeForecast.wsgi:application --bind 0.0.0.0:8000
echo "Starting wsgi"

#python manage.py runserver 0.0.0.0:8000
#echo "Starting runserver"

echo "Finished"
