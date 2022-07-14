"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import django
import os
from django.core.asgi import get_asgi_application
from pathlib import Path
from dotenv import load_dotenv

django.setup()

dotenv_path = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
