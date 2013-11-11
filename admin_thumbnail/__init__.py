__VERSION__ = '0.1.1'

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    settings.INSTALLED_APPS = tuple(settings.INSTALLED_APPS + ('sorl.thumbnail',))
except (ImportError, ImproperlyConfigured), e:
    pass