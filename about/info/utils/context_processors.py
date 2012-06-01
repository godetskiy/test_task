#-*- coding:utf-8 -*-
from django.conf import settings


def add_django_settings(request):
    return {'settings': settings}
