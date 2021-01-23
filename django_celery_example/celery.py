"""
Celery config file

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import

import os
import time

from celery import Celery
from django.conf import settings

# this code copied from manage.py
# set the default Django settings module for the 'celery' app
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery_example.settings")

# change the name here
app = Celery("django_celery_example")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task
def add(x,y):
    print("Hello")
    time.sleep(5)
    return x / y


