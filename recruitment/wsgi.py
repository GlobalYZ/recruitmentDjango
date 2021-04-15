"""
WSGI config for recruitment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
# wsgi是web server gateway interface的简写，Web 服务器网关接口
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recruitment.settings')

application = get_wsgi_application()
