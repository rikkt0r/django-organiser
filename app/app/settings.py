# For more information on this file, see https://docs.djangoproject.com/en/1.8/topics/settings/
# For the full list of settings and their values, see https://docs.djangoproject.com/en/1.8/ref/settings/

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p3o8$1)to2t^t6j4&6-@k==kidtx3t6o&ax*698x80$3kt9(kx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
    'about',
    'users'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'app.urls'

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
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # BACKEND': 'django.core.cache.backends.dummy.DummyCache', (without location)
        'LOCATION': '/home/rikkt0r/PycharmProjects/my-organiser/cache',
        'KEY_PREFIX': 'myorganiser_',
        'TIMEOUT': 3600
    }
}

AUTHENTICATION_BACKENDS = (
    'users.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend'
)

AUTH_PROFILE_MODULE = 'users.UserProfile'
# 2 weeks in seconds
SESSION_COOKIE_AGE = 1209600

LOGIN_REDIRECT_URL = '/users/'
LOGIN_URL = '/users/login/'
LOGOUT_URL = '/users/logout/'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'  # 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = ''
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

MEDIA_ROOT = '/home/rikkt0r/PycharmProjects/my-organiser/media'
MEDIA_URL = '/task/file/'
