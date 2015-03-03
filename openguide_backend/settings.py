"""
Django settings for openguide_backend project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2pd%x(g-o^=ezv7^zgvjf9iixqqq5o8i_ahc29(a%o!@=09x&)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

<<<<<<< HEAD
INSTALLED_APPS = (
=======
INSTALLED_APPS = [
    'file_storage',
>>>>>>> Added views for uploads, added thumbnail generation
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_guide',
    'rest_framework',
    'corsheaders',
    #'file_storage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
<<<<<<< HEAD
)

ROOT_URLCONF = 'openguide_backend.urls'

=======
]

ROOT_URLCONF = 'openguide_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = ( os.path.join(BASE_DIR, 'templates/'), )

# Store messages in the request's session.
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


>>>>>>> Added views for uploads, added thumbnail generation
WSGI_APPLICATION = 'openguide_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'openguide_backend',
        'USER': 'openguide',
        'PASSWORD': 'openstax',
        'HOST': '127.0.0.1',
       
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',),
    'PAGINATE_BY': 10
}

CORS_ORIGIN_ALLOW_ALL = True

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DOCUMENT_ROOT = os.path.join(MEDIA_ROOT, 'filestore')
IMAGE_DOCUMENT_ROOT = os.path.join(DOCUMENT_ROOT, 'images')
<<<<<<< HEAD

=======
MEDIA_URL = '/media/'
DOCUMENT_MEDIA_URL = MEDIA_URL + 'filestore/'
IMAGE_MEDIA_URL = DOCUMENT_MEDIA_URL + 'images/'
>>>>>>> Added views for uploads, added thumbnail generation


try:
    from local_settings import *
except ImportError:
    pass


