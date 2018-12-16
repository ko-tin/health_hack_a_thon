"""
WSGI config for prj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
#from dj_static import Cling #heroku
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
application = get_wsgi_application()
#application = Cling(get_wsgi_application()) #heroku

