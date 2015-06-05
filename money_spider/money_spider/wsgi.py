"""
WSGI config for money_spider project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "money_spider.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
