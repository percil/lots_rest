from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-de-3gq=r&+%)=+kq=iwn=x24)$hd$5!a_g7x-96bwnlekaigm3'

# SECURITY WARNING: define the correct hosts in production!
CSRF_TRUSTED_ORIGINS = ['http://localhost']
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
]
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar'
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = ['127.0.0.1', '172.17.0.1', ]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

try:
    from .local import *
except ImportError:
    pass
