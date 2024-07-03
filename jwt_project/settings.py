from pathlib import Path
from datetime import timedelta
import os
import environ
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@#7%m8uxc)z_2dc6#c*_vkbr6m5o^@*f&93g9&#lkceh_(@&v&'
DEBUG = False
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'jwt_project/static'),
    os.path.join(BASE_DIR, 'dist')
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

env = environ.Env(DEBUG=(bool, False))
root = environ.Path(__file__) - 2
environ.Env.read_env()

TELEGRAM_BOT_NAME = 'DevelopmentMesenevBot'
TELEGRAM_BOT_TOKEN = '7309828847:AAFlb0mZYG6pYlv3CgGkT07U3SSZMRmEX5o'
SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = TELEGRAM_BOT_TOKEN
SECRET_KEY = env.str('SECRET_KEY', '!!! SET YOUR SECRET_KEY !!!')
LOGIN_REDIRECT_URL = reverse_lazy('profile')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.telegram.TelegramAuth',
)

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "https://kbvl.ru"
]
CSRF_TRUSTED_ORIGINS = [
    "https://kbvl.ru",
]
SESSION_COOKIE_HTTPONLY = False
CORS_ALLOW_ALL_ORIGINS = True
CSRF_EXEMPT_VIEW = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'rest_framework_simplejwt',
    'corsheaders',
    'celery_app',
    'jwt_project',
    'django_telegram_login',
    'social_django',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'jwt_project.urls'
WSGI_APPLICATION = 'jwt_project.wsgi.application'

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3', }}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"


TRANSMISSION_HOST = 'transmission'
TRANSMISSION_PORT = 9091
TRANSMISSION_USERNAME = 'VorVZakone'
TRANSMISSION_PASSWORD = '1234'
STATIC_ROOT = 'static'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": 'redis://localhost:6379',
        },
    },
}

CELERY_TIMEZONE = 'Asia/Vladivostok'
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'