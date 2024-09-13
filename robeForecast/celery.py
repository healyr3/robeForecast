from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime, timedelta, timezone

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robeForecast.settings')

app = Celery('robeForecast')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks('riverdata')

app.conf.beat_schedule = {
    'run_fetch': {
        'task': 'robeForecast.tasks.fetch',
        'schedule': crontab(minute=2, hour='*/1'),
    },

    'run_forecast': {
        'task': 'robeForecast.tasks.forecast',
        'schedule': crontab(minute=3, hour='*/1'),
    }
}
