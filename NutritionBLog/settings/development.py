from ._base import *
INTERNAL_IPS=['127.0.0.1',]
#######################DB####################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DemoTest',
        'USER': 'postgres',
        'PASSWORD': 'tomenage1',
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
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static'),]
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
#######################EMAIL###################################
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SERVER_EMAIL='mojserver@gmail.com'