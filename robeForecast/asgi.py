"""
ASGI config for robeForecast project.

It exposes the ASGI callable as a module-level variable named ``riverdata``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robeForecast.settings')

# api = get_asgi_application()
riverdata = get_asgi_application()
