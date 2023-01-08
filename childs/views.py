from django.shortcuts import render
from .models import Employee, Child
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def employees(request):
    """display all employees and properties"""
    employees = Employee.objects.all()
    template = loader.get_template('employees.html')
    context = {
        'employees': employees,
    }

    return HttpResponse(template.render(context, request))