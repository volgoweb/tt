# -*- coding: utf-8 -*-
"""
Django settings for core project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import imp
import sys
import djcelery

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(BASE_DIR, 'lib'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6v2lfkoq*-p#b_-hioxluvb@((1xcny^o9w&)n27z$l8yyj*j&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
    os.path.join(PROJECT_DIR, 'theme_framework_dk', 'templates'),
    os.path.join(PROJECT_DIR, 'theme_framework_dk', 'base', 'templates'),
)

ALLOWED_HOSTS = ['127.0.0.1']
INTERNAL_IPS = ('127.0.0.1',)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'rest_framework',
    # 'south',
    'less',
    'compressor',
    'easy_thumbnails',
    # 'sitetree',
    'ckeditor',
    'autoslug',
    # 'constance',
    # 'constance.backends.database',
    # 'captcha',

    'main.helper',
    'main.theme_framework_dk',
    'main.project',
    'main.task',
    'main.account',
    'main.release',
    'main.specification',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'main.urls'

# WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tt',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PARAMS': {
            'default-character-set': 'utf8',
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = (
	('ru', 'Russian'),
	('en', 'English'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

DATE_INPUT_FORMATS= ('%d.%m.%Y',)
DATE_FORMAT = 'd.m.Y'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
    # 'static',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    'less.finders.LessFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, "files")
MEDIA_URL = '/files/'
# ADMIN_MEDIA_PREFIX = '/files/admin/'
# ADMIN_MEDIA_PREFIX = '/static/admin/'

AUTH_USER_MODEL = 'account.Account'
AUTHENTICATION_BACKENDS = (
    'main.account.auth_backends.AccountModelBackend',
)

FILE_UPLOAD_TEMP_DIR = '/tmp/'

# имя каталога для загрузки картинок разных моделей
IMAGES_UPLOAD_FOLDER = 'images'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    # "constance.context_processors.config",
    "django.contrib.messages.context_processors.messages",
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


# REST FRAMEWORK
REST_FRAMEWORK = {
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
    #     'rest_framework.authentication.TokenAuthentication',
    # ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAdminUser',
    # ),
    'PAGINATE_BY': 10,
    # 'EXCEPTION_HANDLER': 'api.utils.exception_handler',
}


COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

COMPRESS_ROOT = os.path.join(PROJECT_DIR, "static", "less")
COMPRESS_URL = STATIC_URL + 'less/'

# easy_thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'big': {'size': (200, 200), 'crop': True},
        'medium': {'size': (100, 100), 'crop': True},
        'small': {'size': (50, 50), 'crop': True},
    },
}
THUMBNAIL_DEBUG = True

#ckeditor
CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, "ckeditor")
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Basic',
    },
    'full': {
        'width': '100%',
        'toolbar': 'full',
    }
}

# модуль Constance (свои кастомные настройки проекта, которые можно изменять из админки)
# CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
# CONSTANCE_CONFIG = {
#     'SELECT_EMPTY_LABEL': (u'- Выбрать -', u'Название пустого пункта в ниспадающих списках.'),
# }


# подгружаем настройки, для данного сервера
# try:
#     custom_settings_module = imp.load_source('settings_custom', os.path.join(PROJECT_DIR, 'settings_custom.py'))
#     globals().update(vars(custom_settings_module))
# except:
#     print 'ERROR: Additional settings_custom.py load failed. '

# ------------------ 
# Celery and RabbitMQ
os.environ['CELERY_LOADER'] = 'django'
djcelery.setup_loader()
AMQP_HOST = 'localhost'
BROKER_HOST = 'localhost'
BROKER_PORT = 5672
BROKER_VHOST = '/'
BROKER_USER = 'root'
BROKER_PASSWORD = 'root'
INSTALLED_APPS += ('djcelery',)
