from celery import shared_task
from .fetch import *
from .forecast import *


@shared_task()
def run_fetch():
    call_command('fetch')


@shared_task()
def run_forecast():
    call_command('forecast')
