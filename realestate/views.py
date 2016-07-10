#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.shortcuts import render
from django.http import HttpResponse

from .models import Property
from .forms import PropertyForm


# Create your views here.

def real_estate_index(request):
    if request.method == 'GET':
        submission_form = PropertyForm()
        context = {
            'submission_form': submission_form,
        }
        return render(request, 'realestate/index.html', context)
    else:
        return render(request, 'realestate/index.html', {
            'title': request.POST['title'],
        })
