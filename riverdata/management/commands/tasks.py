from celery import shared_task
from .fetch import *
from .forecast import *

@shared_task
def run_fetch_data():
    call_command('fetch_data')

@shared_task
def run_forecast():
    call_command('forecast')
