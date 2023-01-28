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


def childs(request):
    "display all childs of the employee"
    nCode = request.GET['nCode']
    employee = Employee.objects.filter(nationalCode=nCode)
    childs = Child.objects.filter(parent=employee[0])
    context = {
        'employee': employee, 
        'childs': childs,
    }
    
    template = loader.get_template('childs.html')
    return HttpResponse(template.render(context, request))