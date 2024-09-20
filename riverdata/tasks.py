from celery import shared_task
from django.core.management import call_command

# @shared_task()
# def run_fetch():
#     call_command('fetch')
#
# @shared_task()
# def run_forecast():
#     call_command('forecast')
@shared_task()
def run_fetch_forecast_metrics():
    call_command('fetch')
    call_command('forecast')
    call_command('metrics')
