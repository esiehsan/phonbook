from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from django.template import loader
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .forms import RegForm

# Create your views here.
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
    
    # template = loader.get_template('all_person.html')
    context = {
        'persons': persons,
    }
       
    return render(request, 'all_person.html', context)


def detail(request, person_id):
    person = get_object_or_404(Person, id = person_id)

    context = {'person': person}
    return render(request, 'detail.html', context)