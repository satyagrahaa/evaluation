from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Attribute


# Create your views here.
def index(request):
    recently_added = Employee.objects.all()
    output = '\n'.join([e.name for e in recently_added])
    return HttpResponse(output)

def points(request):
    recently_added = Employee.objects.all()
    output = '\n'.join([e.name for e in recently_added])
    return HttpResponse(output)

