DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

INSTALLED_APPS += (
	'gunicorn',
)