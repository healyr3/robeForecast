from celery import shared_task
from django.core.management import call_command
import logging

logger = logging.getLogger(__name__)

@shared_task()
def run_fetch():
    logger.info('Running fetch....')
    call_command('fetch')


@shared_task()
def run_forecast():
    call_command('forecast')
