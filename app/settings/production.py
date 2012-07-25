from default import *
import dj_database_url
# Django production settings for app project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

INSTALLED_APPS += (
    'gunicorn',
)
