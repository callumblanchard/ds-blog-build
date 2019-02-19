"""
Django dev settings for dsblog project.

Variables are imported from settings.py.
Any variables that differ from local can be redefined here.
"""

import os
from .settings import *

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['1ezq8xfzx8.execute-api.eu-west-2.amazonaws.com']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'), # dbname
        'USER': os.getenv('DB_USER'), # master username
        'PASSWORD': os.getenv('DB_PASSWORD'), # master password
        'HOST': os.getenv('DB_ENDPOINT'), # Endpoint
        'PORT': '3306',
    }
}
