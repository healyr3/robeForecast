from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging

from celery.signals import setup_logging
from django.conf import settings

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

@app.task(bind=True)
def debug_task(self):
    # print(f'Request: {self.request!r}')
    print('Request: {0!r}'.format(self.request))

@setup_logging.connect
def config_loggers(*args, **kwargs):
    logging.config.dictConfig(settings.LOGGING)

# from celery.schedules import crontab
# from datetime import datetime, timedelta, timezone

# app.conf.beat_schedule = {
#     'run_fetch': {
#         'task': 'robeForecast.tasks.fetch',
#         'schedule': crontab(minute=2, hour='*/1'),
#     },
#
#     'run_forecast': {
#         'task': 'robeForecast.tasks.forecast',
#         'schedule': crontab(minute=3, hour='*/1'),
#     }
# }
