#-*- coding:utf-8 -*-
from django.contrib import admin
from info.models import Person, LogRequest, LogModel


class PersonAdmin(admin.ModelAdmin):
    pass


class LogRequestAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'host', 'path', 'method')
    ordering = ('-datetime',)


class LogModelAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'model_name', 'action')
    ordering = ('-datetime',)

admin.site.register(Person, PersonAdmin)
admin.site.register(LogRequest, LogRequestAdmin)
admin.site.register(LogModel, LogModelAdmin)
