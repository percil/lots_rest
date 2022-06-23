import logging

from .base import *

logger = logging.getLogger('prod')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
REST_URL = os.getenv('REST_URL')
FRONT_URL = os.getenv('FRONT_URL')

# SECURITY WARNING: define the correct hosts in production!
CSRF_TRUSTED_ORIGINS = [f'https://{REST_URL}', f'https://{FRONT_URL}']
ALLOWED_HOSTS = [FRONT_URL, REST_URL]

CORS_ALLOWED_ORIGINS = [
    f'https://{FRONT_URL}',
]

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
