# https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_wsgi_application()
