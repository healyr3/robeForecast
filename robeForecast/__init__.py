# myproject/__init__.py
from __future__ import absolute_import, unicode_literals

# Django starts so that shared_task will use this app.
from robeForecast.celery import app as celery_app

__all__ = ('celery_app',)
