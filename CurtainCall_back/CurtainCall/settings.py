"""
Django settings for CurtainCall project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
#삭제바람

from pathlib import Path
import os
# from CurtainCall.donotcommit.aws_s3 import s3_config as s3
from CurtainCall.donotcommit import postgre as pg
from CurtainCall.donotcommit import aws_s3 as s3
# from CurtainCall.donotcommit import oauth2 as oa

from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0d(z=n2&n22ha7#a_)z2i^n0t1o5t1=5z%kmps7rh##%cd7la9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
#    'allauth.socialaccount',
#    'allauth.socialaccount.providers.google',


    'rest_framework',
    #'rest_framework_simplejwt.token_blacklist',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',

    'drf_yasg',
    'storages',
    "channels",
    'corsheaders',

    'CurtainCallApp.apps.CurtaincallappConfig',
    'Stage.apps.StageConfig',
    'Image.apps.ImageConfig',
    'Algorithm_cv2.apps.AlgorithmCv2Config',
    'accounts',



]



AUTH_USER_MODEL = 'accounts.User'


JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

REST_AUTH = {
    'USE_JWT': True,
    'SESSION_LOGIN': False,
    'JWT_AUTH_HTTPONLY': False,
}

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # 개발 중에는 콘솔 백엔드 사용

#AUTHENTICATION_BACKENDS = [
#    'django.contrib.auth.backends.ModelBackend',
#    'allauth.account.auth_backends.AuthenticationBackend',
#]

REST_USE_JWT = True

SITE_ID = 1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', # 인증된 사용자만 접근
        # 'rest_framework.permissions.IsAdminUser', # 관리자만 접근
        #'rest_framework.permissions.AllowAny',  # 누구나 접근
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}


REST_AUTH_TOKEN_MODEL = None

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'dj_rest_auth.serializers.JWTSerializer',
}

#LOGIN_URL = '/'
#LOGIN_REDIRECT_URL = '/'
#LOGOUT_REDIRECT_URL = '/'
#SOCIAL_AUTH_URL_NAMESPACE = 'social'

#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = oa.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = oa.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET


CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000", "https://localhost:8000","http://0.0.0.0:8000"]

#set below setting value to False if you want to store images at s3 Server
USE_LOCAL_IMAGES = False

if(not USE_LOCAL_IMAGES):
    class AWS_S3:
        AWS_ACCESS_KEY_ID = s3.AWS_ACCESS_KEY_ID
        AWS_SECRET_ACCESS_KEY = s3.AWS_SECRET_ACCESS_KEY
        AWS_REGION = s3.AWS_REGION

        AWS_STORAGE_BUCKET_NAME = s3.AWS_STORAGE_BUCKET_NAME
        AWS_S3_CUSTOM_DOMAIN = s3.AWS_S3_CUSTOM_DOMAIN
        AWS_S3_OBJECT_PARAMETERS = s3.AWS_S3_OBJECT_PARAMETERS
        DEFAULT_FILE_STORAGE = s3.DEFAULT_FILE_STORAGE
        MEDIA_ROOT = os.path.join(BASE_DIR, 'path/to/store/my/files/')


MIDDLEWARE = [
    #corsheaders 맨 위에 둘 것 / CommonMiddleware은 이미 포함되어있어서 미추가했는데 추후에 필요하다면 밑 줄에 추가할 것.
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    'http://localhost:8000',
    'http://0.0.0.0:8000',
    'http://0.0.0.0:3000',
    'http://3.131.38.82:3000'
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    'http://localhost:8000',
    "http://0.0.0.0:3000",
    'http://0.0.0.0:8000',
    'http://3.131.38.82:3000'
]

# CORS_ORIGIN_WHITELIST = [
#     'http://127.0.0.1:3000',
#     'http://localhost:3000',
#     'http://3.131.38.82:3000'
# ]
# CORS_ALLOW_ALL_ORIGINS = True #(모든 포트 허용)

ROOT_URLCONF = 'CurtainCall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

# settings.py



#LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'CurtainCall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': pg.database_name,
        'USER': pg.database_user,
        'PASSWORD': pg.PASSWORD,
        'HOST': pg.HOST,
        'PORT': pg.PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media filesx
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# WebSocket 관련 설정
ASGI_APPLICATION = 'your_project_name.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',  # 채널 레이어 설정 (실제 환경에서는 다른 백엔드를 사용할 수 있음)
    },
}

