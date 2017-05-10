from .base import *
import os

#Para settear este archivo como el settings local se debe ejecutar esto:
#export DJANGO_SETTINGS_MODULE=goodreads.settings.local

SECRET_KEY = 'oeeoww9^v6!)57-_!d)ar@8h0#zj)utg^-b(o-8$rjhfb7kqqf'
#SECRET_KEY =os.getenv('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'goodreads_db',
        'USER': 'goodreads_admin',
        'PASSWORD': '12345',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
