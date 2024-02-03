"""
Конфигурация WSGI для проекта djangoProject.

Она предоставляет вызываемый WSGI в качестве переменной уровня модуля с именем `application`.

Для получения дополнительной информации об этом файле смотрите
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

application = get_wsgi_application()
