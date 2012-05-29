#-*- coding:utf-8 -*-
from django import forms
from django.forms import ModelForm
from info.models import Person

class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('css/ui-lightness/jquery-ui.css',),
        }

        js = ("js/jquery-1.7.2.min.js",
              "js/jquery-ui-1.8.20.custom.min.js",
              "js/ui.datepicker-ru.js",
        )

class PersonForm(ModelForm):
    class Meta:
        model = Person

        #get reverse fields_list
        fields_list = list()
        for field in Person._meta.fields:
            fields_list.append(field.get_attname())
        fields_list.reverse()
        fields = fields_list

        widgets = {
            'bdate': CalendarWidget,
        }
