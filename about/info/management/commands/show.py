#-*- coding:utf-8 -*-
from django.core.management.base import AppCommand

class Command(AppCommand):
    help = 'Print all models and the count of objects in given app'
    args = '[appname]'
    requires_model_validation = True

    def handle_app(self, app, **options):
        from django.db.models import get_models

        lines = []

        for model in get_models( app ):
            lines.append( "[%s] - %s objects" % (model.__name__, model._default_manager.count()))

        return "\n".join( lines )
