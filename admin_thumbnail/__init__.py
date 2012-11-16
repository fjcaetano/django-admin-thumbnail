__VERSION__ = '0.1.1'

from django.conf import settings

try:
    settings.INSTALLED_APPS = tuple(settings.INSTALLED_APPS + ('sorl.thumbnail',))
except ImportError, e:
    pass