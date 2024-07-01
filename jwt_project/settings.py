from pathlib import Path
from datetime import timedelta
import os
import environ
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@#7%m8uxc)z_2dc6#c*_vkbr6m5o^@*f&93g9&#lkceh_(@&v&'
DEBUG = True
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'jwt_project/static'),
    # os.path.join(BASE_DIR, 'dist')
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

TELEGRAM_BOT_NAME = 'VideoDownloadTG_bot'
TELEGRAM_BOT_TOKEN = '7234654837:AAF_J6GRNPS9EMguhUYFtKXhyjV1FLsCOuI'
SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = "7234654837:AAF_J6GRNPS9EMguhUYFtKXhyjV1FLsCOuI"
SECRET_KEY = env.str('SECRET_KEY', '!!! SET YOUR SECRET_KEY !!!')
LOGIN_REDIRECT_URL = reverse_lazy('profile')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.telegram.TelegramAuth',
)

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "https://da3c-185-57-28-150.ngrok-free.app"
]
CSRF_TRUSTED_ORIGINS = [
    "https://da3c-185-57-28-150.ngrok-free.app",
]
SESSION_COOKIE_HTTPONLY = False
CORS_ALLOW_ALL_ORIGINS = True
CSRF_EXEMPT_VIEW = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    )
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
    'jwt_project',
    'django_telegram_login',
    'social_django',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
