from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiblioteca',
        'USER':'ahiezer',
        'PASSWORD':'ASDqwe123',
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