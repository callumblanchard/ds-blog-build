"""
Django dev settings for dsblog project.
"""

import os
from .settings import *

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['lza3lkdjfc.execute-api.eu-west-2.amazonaws.com']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pollsdb', # dbname
        'USER': 'polls_admin', # master username
        'PASSWORD': 'pollsadmin', # master password
        'HOST': 'pollsapi-cluster.cluster-chcxxxxx.us-east-2.rds.amazonaws.com', # Endpoint
        'PORT': '3306',
    }
}
