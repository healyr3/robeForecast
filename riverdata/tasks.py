from celery import shared_task
from django.core.management import call_command
import logging

logger = logging.getLogger(__name__)

# @shared_task()
# def run_fetch():
#     logger.info('Running fetch....')
#     call_command('fetch')

# @shared_task()
# def run_fetch():
#     logger.info('Start Testing Fetch')
#     print('Start Testing Fetch')
#     try:
#         logger.info('Running fetch....')
#         print('Running fetch....')
#         call_command('fetch')
#         logger.info('Fetch command completed successfully.')
#         print('Fetch command completed successfully.')
#     except Exception as e:
#         logger.error(f'Error occurred while running fetch command: {e}')
#         print('Error occurred while running fetch command.')

@shared_task()
def run_fetch():
    logger.info('Task has started.')
    print('Task has started.')
    try:
        logger.info('Calling fetch command...')
        print('Calling fetch command...')
        call_command('fetch')
        logger.info('Fetch command completed successfully.')
        print('Fetch command completed successfully.')
    except Exception as e:
        logger.error(f'Error occurred: {e}')
        print(f'Error: {e}')

@shared_task()
def run_forecast():
    call_command('forecast')
