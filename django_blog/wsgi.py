"""
WSGI config for django_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings")

application = get_wsgi_application()
#wsgi z pythonanywhere
#import os
#import sys
#
#path = '/home/polrider/Django-blog'
#if path not in sys.path:
#    sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'django_blog.settings'
#
#from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise
#application = DjangoWhiteNoise(get_wsgi_application())
