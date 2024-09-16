from celery import shared_task
from django.core.management import call_command
import logging

logger = logging.getLogger(__name__)

# @shared_task()
# def run_fetch():
#     logger.info('Running fetch....')
#     call_command('fetch')

@shared_task()
def run_fetch():
    print('Testing Fetch')
    try:
        logger.info('Running fetch....')
        call_command('fetch')
        logger.info('Fetch command completed successfully.')
    except Exception as e:
        logger.error(f'Error occurred while running fetch command: {e}')

@shared_task()
def run_forecast():
    call_command('forecast')
