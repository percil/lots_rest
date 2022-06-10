import logging

from .base import *

logger = logging.getLogger('prod')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

logger.warning(f'secret_key={SECRET_KEY}')

# SECURITY WARNING: define the correct hosts in production!
CSRF_TRUSTED_ORIGINS = ['https://lots.percil.be']
ALLOWED_HOSTS = ['lots.percil.be', '*']

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
