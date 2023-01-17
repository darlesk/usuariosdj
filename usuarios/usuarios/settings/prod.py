from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER':get_secret('USER'),
        'PASSWORD':get_secret('PASSWORD'),
        'HOST':'localhost',
        'PORT':'5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#Ru
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/'static']
# O puede ser asi tambien
#STATICFILES_DIRS = ['/home/ahiezer/proyectos/dj/empleado/static']
STATIC_ROOT = BASE_DIR/'staticfiles'

#Ruta para los archivos multimedia
MEDIA_URL = '/media/'
#carpeta base o carpeta raiz donde van a estar almacenados todos nuestros archivos multimedia
MEDIA_ROOT = BASE_DIR/'media'