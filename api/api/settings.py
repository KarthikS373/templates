import os

from pathlib import Path
from api import is_true, split_with_comma

BASE_DIR = Path(__file__).resolve().parent.parent

INSECURE_KEY = 'django-insecure-0eikswwglid=ukts4l2_b=676m!-q_%154%2z@&l3)n6)cp3#c'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', INSECURE_KEY)

DEBUG = is_true(os.getenv('DJANGO_DEBUG', 'true'))

ALLOWED_HOSTS = split_with_comma(os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost'))

INTERNAL_IPS = ['127.0.0.1']

if DEBUG:
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'

DATABASES = {

}

if 'POSTGRES_DB' in os.environ:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT'],
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = os.getenv('DJANGO_LANGUAGE_CODE', 'en-us')

TIME_ZONE = os.getenv('DJANGO_TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# MEDIA_ROOT = os.environ['DJANGO_MEDIA_ROOT']

MEDIA_URL = os.getenv('DJANGO_MEDIA_URL', 'media/')

STATIC_URL = 'static/'

STATIC_ROOT = os.environ['DJANGO_STATIC_ROOT']

STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Sessions
SESSION_COOKIE_SECURE = is_true(os.getenv('DJANGO_SESSION_COOKIE_SECURE'))

# Settings for CSRF cookie.
CSRF_COOKIE_SECURE = is_true(os.getenv('DJANGO_CSRF_COOKIE_SECURE'))
CSRF_TRUSTED_ORIGINS = split_with_comma(os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS', ''))

# Security Middleware (manage.py check --deploy)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 2  # 2 weeks, default - 0
SECURE_SSL_REDIRECT = is_true(os.getenv('DJANGO_SECURE_SSL_REDIRECT'))
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Email settings
EMAIL_HOST = os.getenv('DJANGO_EMAIL_HOST', 'localhost')
EMAIL_PORT = int(os.getenv('DJANGO_EMAIL_PORT', 25))
EMAIL_HOST_USER = os.getenv('DJANGO_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('DJANGO_EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = is_true(os.getenv('DJANGO_EMAIL_USE_TLS'))

# Email address that error messages come from.
SERVER_EMAIL = os.getenv('DJANGO_SERVER_EMAIL', 'root@localhost')

# Default email address to use for various automated correspondence from the site managers.
DEFAULT_FROM_EMAIL = os.getenv('DJANGO_DEFAULT_FROM_EMAIL', 'webmaster@localhost')

# People who get code error notifications. In the format
# [('Full Name', 'email@example.com'), ('Full Name', 'anotheremail@example.com')]
ADMIN_NAME = os.getenv('DJANGO_ADMIN_NAME', '')
ADMIN_EMAIL = os.getenv('DJANGO_ADMIN_EMAIL')
if ADMIN_EMAIL:
    ADMINS = [(ADMIN_NAME, ADMIN_EMAIL)]

CELERY_APP = 'api.celery:app'

# Log settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname}: {message}',
            'style': '{',
        },
        'error_format': {
            'format': '[{asctime}] ERROR: {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True, 
            'formatter': 'error_format',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'] if not DEBUG else ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
