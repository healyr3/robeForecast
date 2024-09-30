from __future__ import absolute_import, unicode_literals
import os
import logging

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robeForecast.settings')

# Create a Celery instance
app = Celery('robeForecast')

# Using a string here means the worker doesn’t have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Set up logging for Celery
logger = logging.getLogger('celery')
logger.setLevel(logging.INFO)

app.conf.beat_schedule = {
    'run_fetch_forecast': {
        'task': 'riverdata.tasks.run_fetch_forecast_metrics',
        'schedule': crontab(minute='2', hour='*/1'),
    }
}
