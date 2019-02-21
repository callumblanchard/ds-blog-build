"""
Django dev settings for dsblog project.

Variables are imported from settings.py.
Any variables that differ from local can be redefined here.
"""

import os
from .settings import *

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['1ezq8xfzx8.execute-api.eu-west-2.amazonaws.com','d323zg9w1czp77.cloudfront.net']

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'], # dbname
        'USER': os.environ['DB_USER'], # master username
        'PASSWORD': os.environ['DB_PASSWORD'], # master password
        'HOST': os.environ['DB_ENDPOINT'], # Endpoint
        'PORT': '3306',
    }
}
