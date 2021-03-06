"""
Django settings for DjangoWebProject5 project.

Generated by 'django-admin startproject' using Django 1.9.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import posixpath

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e1326ec9-f321-4114-a06f-a08f77c42e4f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # django uygulamaları
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #kendi uygulamalarım
    'post',
#3. parti uygulamalar
    'crispy_forms',#form tasarımı için
    'django_cleanup',#veri silmek için foto vs
    'ckeditor',#formlara italik vs özellik toolları vermek için
    'captcha',#captcha yazılımu için


]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoWebProject5.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'DjangoWebProject5.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'#bootstrap jquery için
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
    ]

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles/')
CRISPY_TEMPLATE_PACK = 'bootstrap3'#yeni form tasarımı için
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')#upload edilen şeyler veritabanı yerine media adlı klasörde yer alması için
CKEDITOR_JQUERY_URL =os.path.join(STATIC_URL,'js/jquery.min.js')
CKEDITOR_CONFIGS = {
    'default': {
        
        #'toolbar': 'full',
       # 'height': 300,
        'width': '100%',
    },
}
RECAPTCHA_PUBLIC_KEY = '6Lc66HUUAAAAAL-xybKKjE80jLTaUesjChpb4ZHh'
RECAPTCHA_PRIVATE_KEY = '6Lc66HUUAAAAALcsNeP3bDLb1n2ag4GPw3afuGRK'
NOCAPTCHA=True