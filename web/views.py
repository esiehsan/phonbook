from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .forms import RegForm

# Create your views here.
@csrf_exempt  #remove check for csrf cookie
def persons(request):
    """check request method. if method is post save search_phrase and 
    filter data in person table and return http that make with all_person.html 
    template
    """
    if len(request.GET):
        search_phrase = request.GET['searchtext']
        persons = Person.objects.filter(Q(fName__contains=search_phrase) | Q(lName__contains=search_phrase)).values()
    else:
        persons = Person.objects.all()
    
    template = loader.get_template('all_person.html')
    context = {
        'persons': persons,
    }
       
    return HttpResponse(template.render(context, request))

def register(request):
    form = RegForm()
    template = loader.get_template('register.html')
    context = {
        'form' : form,
    }

    return HttpResponse(template.render(context, request))

def detail(request, person_id):
    return HttpResponse('detail of person records: '+ str(person_id))