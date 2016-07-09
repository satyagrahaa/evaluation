#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django import forms

from .models import Employee, Attribute


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'job_title', ]


class AttributeModelForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ['employee', 'teamwork', 'creativity', 'discipline', 'spirit', ]
