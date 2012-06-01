#-*- coding:utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


class Person(models.Model):
    name = models.CharField(_(u'Имя'), max_length=30)
    surname = models.CharField(_(u'Фамилия'), max_length=50)
    bdate = models.DateField(_(u'Дата рождения'))
    email = models.EmailField()
    contacts = models.TextField(_(u'Контакты'), blank=True)
    bio = models.TextField(_(u'Биография'), blank=True)

    def __unicode__(self):
        return "%s %s" % (self.surname, self.name)


class LogRequest(models.Model):
    datetime = models.DateTimeField(default=datetime.now())
    host = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=255)

    def __unicode__(self):
        return self.datetime


class LogModel(models.Model):
    datetime = models.DateTimeField(default=datetime.now())
    model_name = models.CharField(max_length=50)
    action = models.CharField(max_length=7)

    def __unicode__(self):
        return u'%s %s %s' % (str(self.datetime), self.model_name, self.action)


@receiver(post_save, sender=Person)
@receiver(post_save, sender=LogRequest)
def create_edit_handler(instance, created, **kwargs):
    action = 'create' if created else 'edit'
    ctype = ContentType.objects.get_for_model(instance)
    l = LogModel(model_name=ctype.model.title().encode(), action=action)
    l.save()


@receiver(post_delete, sender=Person)
@receiver(post_delete, sender=LogRequest)
def delete_handler(instance, **kwargs):
    ctype = ContentType.objects.get_for_model(instance)
    l = LogModel(model_name=ctype.model.title().encode(), action='delete')
    l.save()
