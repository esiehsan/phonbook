from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person

# Create your views here.
def all_persons(request):
    persons = Person.objects.all().values()
    template = loader.get_template('all_person.html')
    context = {
        'persons': persons,
    }
    return HttpResponse(template.render(context, request))