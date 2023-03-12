"""
Django settings for ecomprj project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# import django_heroku

from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-%o9!c3rf02q6usr!vw^s96^t*(dsv&ezbs)_u_k7^z1oa$ik0r'

# # Use config value to replace information for security
# SECRET_KEY = config('SECRET KEY')

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# Read secret key from a file
# with open('/etc/secret_key.txt') as f:
#     SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False

ALLOWED_HOSTS = ['nextit12.herokuapp.com', '127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',


    # From django library
    'taggit',
    'ckeditor',
    'bootstrap_datepicker_plus',
    'bootstrap4',
    

    #  Integration of paypal
    'paypal.standard.ipn',

    # Installed Apps
    'core',
    'userauths',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecomprj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'core.context_processor.default',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecomprj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# set static root to static folder in base directory
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# set static directories to point to static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# set media path
MEDIA_URL = '/media/'

# set media root to media folder
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# jazzmin custom settings for admin panel
JAZZMIN_SETTINGS = {
    'site_header': "Nestify Shop",
    'site_brand': "Customer satisfaction is our priority",
    'site_logo': "assets/imgs/theme/loading.gif",
    'copyright': "nestify.com",
}

LOGIN_URL = "userauths:sign-in"
LOGIN_REDIRECT_URL = "core:index"
LOGOUT_REDIRECT_URL = "userauths:sign-in"

AUTH_USER_MODEL = 'userauths.User'

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'codeSnippet_theme': 'monokai',
        'toolbar': 'all',
        'extraPlugins': ','.join(
            [
                'codesnippet',
                'widget',
                'dialog'
            ]
        ),
    }
}


PAYPAL_RECEIVER_EMAIL = 'nestifystore@gmail.com'
PAYPAL_TEST = True

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CSRF_TRUSTED_ORIGINS = [
    'https://nextit12.herokuapp.com/'
]