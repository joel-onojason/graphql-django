from .base import *

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': config("POSTGRES_DB"),
        'USER': config("POSTGRES_USER"),
        'PASSWORD': config("POSTGRES_PASSWORD"),
        'HOST': config("POSTGRES_HOST"),
        'PORT': 5432,
    }
}
