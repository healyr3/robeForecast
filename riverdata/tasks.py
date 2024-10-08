from celery import shared_task
from django.core.management import call_command

@shared_task()
def run_fetch_forecast_metrics():
    call_command('fetch')
    call_command('forecast')
    call_command('metrics')
