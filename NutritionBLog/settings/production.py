from ._base import *
##########################EMAIL##################################
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER=get_secret("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=get_secret("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS=True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
###########################DB##################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret("DATABASE_NAME"),
        'USER': get_secret("DATABASE_USER"),
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        'HOST':get_secret("DATABASE_HOST"),
        'PORT':'5432',
    }
}
########################STATIC###########################
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID=get_secret("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=get_secret("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME=get_secret("AWS_STORAGE_BUCKET_NAME")
AWS_S3_FILE_OVERWRITE=False

AWS_S3_REGION_NAME='eu-central-1'
AWS_S3_HOST = 'eu-central-1.amazonaws.com'
AWS_DEFAULT_ACL=None
AWS_S3_SIGNATURE_VERSION='s3v4'
#######################CACHES###################################
CACHES={
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': get_secret("MEMCACHED_ENDPOINT"),
        'TIMEOUT': 3600*3,
    }

}