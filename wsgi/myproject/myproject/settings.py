"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# /////////////////////////////////////////////////////////////////////////////
#
# Local Config
#
# /////////////////////////////////////////////////////////////////////////////
#
# Set default shell environment variables. 
#
# These should already be set on the Openshift environment and are for the
# local dev environment. If you encounter problems, try just commenting them
# out.
import os
os.environ.setdefault('OPENSHIFT_DATA_DIR', '/home/kovaka/Projects/recordstore/data/')
os.environ.setdefault('OPENSHIFT_APP_DNS', 'recordstore-kovaka.rhcloud.com')
os.environ.setdefault('OPENSHIFT_MYSQL_DB_USERNAME', 'adminmn7uZyV')
os.environ.setdefault('OPENSHIFT_MYSQL_DB_PASSWORD', '4r7gIuZKGPRB')
os.environ.setdefault('OPENSHIFT_MYSQL_DB_HOST', '127.0.0.1')
os.environ.setdefault('OPENSHIFT_MYSQL_DB_PORT', '3306')
os.environ.setdefault('DEBUG', 'True')

# /////////////////////////////////////////////////////////////////////////////
#
# Modify the code below this line at your own risk
#
# /////////////////////////////////////////////////////////////////////////////

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_NAME = 'myproject'
DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
WSGI_DIR = os.path.dirname(BASE_DIR)
REPO_DIR = os.path.dirname(WSGI_DIR)
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', BASE_DIR)

import sys
sys.path.append(os.path.join(REPO_DIR, 'libs'))
import secrets
SECRETS = secrets.getter(os.path.join(DATA_DIR, 'secrets.json'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == 'True'

from socket import gethostname
ALLOWED_HOSTS = [
    'localhost',
    gethostname(), # For internal OpenShift load balancer security purposes.
    os.environ.get('OPENSHIFT_APP_DNS'), # Dynamically map to the OpenShift gear name.
    #'example.com', # First DNS alias (set up in the app)
    #'www.example.com', # Second DNS alias (set up in the app)
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = PROJECT_NAME + '.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = PROJECT_NAME + '.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recordstore',
        'USER': os.environ.get('OPENSHIFT_MYSQL_DB_USERNAME'),
        'PASSWORD': os.environ.get('OPENSHIFT_MYSQL_DB_PASSWORD'),
        'HOST': os.environ.get('OPENSHIFT_MYSQL_DB_HOST'),
        'PORT': os.environ.get('OPENSHIFT_MYSQL_DB_PORT'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
from django.conf import settings

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(WSGI_DIR, 'static')
