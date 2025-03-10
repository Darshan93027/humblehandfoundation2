import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HumbleHandFoundation.settings')

app = Celery('HumbleHandFoundation')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat Settings
app.conf.update(
    BROKER_CONNECTION_RETRY=True,
    BROKER_CONNECTION_RETRY_ON_STARTUP=True,
    BROKER_CONNECTION_MAX_RETRIES=5,
)

# Load task modules from all registered Django apps.
app.autodiscover_tasks() 