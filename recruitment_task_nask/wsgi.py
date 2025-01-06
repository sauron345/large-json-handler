"""
WSGI config for recruitment_task_nask project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

import atexit

from .startup import close_knowledge_base

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recruitment_task_nask.settings')

application = get_wsgi_application()

atexit.register(close_knowledge_base)
