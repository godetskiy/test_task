#-*- coding:utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from info.models import Person
from info.forms import PersonForm


def person(request):
    info = get_object_or_404(Person)
    return render_to_response('person.html', {'title': 'Информация', 'info': info})


@login_required()
def person_edit(request):
    c = {}
    c.update(csrf(request))
    c['title'] = u'Редактирование данных'

    person = Person.objects.get()
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = PersonForm(instance=person)
    c['form'] = form
    return render_to_response('form.html', c)
