"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
root = os.path.dirname(__file__)                                             #输出当前文件所在文件夹的绝对路径
sys.path.insert(0, os.path.join(root, '..', 'site-packages'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
