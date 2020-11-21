import os

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application

from project import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()


if settings.DEBUG and settings.USE_STATIC_FILE_HANDLER_FROM_WSGI:
    application = StaticFilesHandler(get_wsgi_application())
else:
    application = get_wsgi_application()
