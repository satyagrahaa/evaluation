#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.shortcuts import render
from django.http import HttpResponse

from .models import Employee, Attribute
from .forms import EmployeeModelForm, AttributeModelForm


# Create your views here.



def index(request):
    recently_added = Employee.objects.all()
    output = '\n'.join([e.name for e in recently_added])
    return HttpResponse(output)


def indexx(request, employee_name):
    output = employee_name
    return HttpResponse(output)


def points(request):
    employees = Employee.objects.order_by('name')
    form = EmployeeModelForm()
    context = {
        'employees': employees,
        'form': form,
    }
    return render(request, 'eval_app/index.html', context)
