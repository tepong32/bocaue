from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "y*#&b#rjamr&_6eg2-_^5bt8j=$#@t=roch6&ocy4_if-at9y8"

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAIL_CACHE = False

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
