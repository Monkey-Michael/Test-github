"""
Django settings for CJST_Connector project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k^y!p^3n7esf)e4ha4^mxr0hsr6krhggf9m68%li3a*)^865m&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['120.79.57.43','www.cjst-dg.com','api.cjst.site','localhost','0.0.0.0:8000']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'haystack',
    'xadmin',
    'crispy_forms',
    'reversion',
    'rest_framework',
    'ckeditor',
    'ckeditor_uploader',
    'user.apps.UserConfig',
    'goods.apps.GoodsConfig'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CJST_Connector.urls'

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

WSGI_APPLICATION = 'CJST_Connector.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_demo',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'W9874wlx+!'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

#Haystack

HAYSTACK_CONNECTIONS = {
    'default':{
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR,'whoosh_index')
    }

}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

#设置每页显示的数目，默认为20，可以自己修改
HAYSTACK_SEARCH_RESULTS_PER_PAGE  =  10

#REST_FRAME RESPONSE
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (  # 默认响应渲染类
        'rest_framework.renderers.JSONRenderer',  # json渲染器
        'rest_framework.renderers.BrowsableAPIRenderer',  # 浏览API渲染器
    )
}



#Cors
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8000',
    '127.0.0.1:8020',
    '120.79.57.43',
    '120.79.57.43:8001',
    '120.79.57.43:8000',
    '0.0.0.0:8000',
    'www.cjst-dg.com'

)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)



CORS_ORIGIN_ALLOW_ALL = True



CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# #QINIU Upload
# QINIU_ACCESS_KEY = "yV4GmNBLOgQK-1Sn3o4jktGLFdFSrlywR2C-hvsW"
# QINIU_SECRET_KEY = "bixMURPL6tHjrb8QKVg2tm7n9k8C7vaOeQ4MEoeW"
# QINIU_BUCKET_NAME = "ihome"
# QINIU_BUCKET_DOMAIN = 'ompehspge.bkt.clouddn.com/'
# QINIU_SECURE_URL = False      #使用http
#
# PREFIX_URL = 'http://'
#
# MEDIA_URL = PREFIX_URL + QINIU_BUCKET_DOMAIN + '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#
# DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
#
#静态文件存储
#STATIC_URL = PREFIX_URL +QINIU_BUCKET_DOMAIN + '/static/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATICFILES_DIRS = [
    ("css", os.path.join(STATIC_ROOT, 'css')),
    ("img", os.path.join(STATIC_ROOT, 'img')),
    ("js", os.path.join(STATIC_ROOT, 'js')),
]



#STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'

#Ckeditor Config
CKEDITOR_CONFIGS = {
    'default':{
        'toolbar' : 'full',
        'height': 300,

    }
}
CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR,'media/editor_images')
