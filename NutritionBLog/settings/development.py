from ._base import *
INTERNAL_IPS=['127.0.0.1',]
#######################DB####################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'NutriBlog',
        'USER': 'postgres',
        'PASSWORD': 'upaljacb1',
        'HOST':'localhost',
        'PORT':'5432',
    }
}
##########################CACHE#############################
CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 10#3600*360,
    }

}
####################STATIC###################################
#STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
#######################EMAIL###################################
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH='temp/emails/'
SERVER_EMAIL='mojserver@gmail.com'
#####################LOGING####################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

WEBSITE_URL='localhost:8000'