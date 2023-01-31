from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.
@csrf_exempt  #remove check for csrf cookie
def all_persons(request):
    """check request method. if method is post save search_phrase and 
    filter data in person table and return http that make with all_person.html 
    template
    """
    if(request.method == 'POST'):
        search_phrase = request.POST['searchtext']
    else:
        search_phrase = ''
    
    persons = Person.objects.filter(Q(fName__contains=search_phrase) | Q(lName__contains=search_phrase)).values()
    template = loader.get_template('all_person.html')
    context = {
        'persons': persons,
    }
       
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))