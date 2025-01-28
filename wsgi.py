"""
WSGI config for neem_karoli_travellers project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Set the default settings module for the 'django' program.
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    os.getenv('DJANGO_SETTINGS_MODULE', 'neem_karoli_travellers.settings')
)

# Initialize the application.
application = get_wsgi_application()

# Add WhiteNoise for serving static files.
application = WhiteNoise(application)

# Log WSGI application initialization.
import logging
logger = logging.getLogger(__name__)
logger.info('WSGI application initialized.')
