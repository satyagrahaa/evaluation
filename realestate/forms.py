#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django import forms

from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'owner', 'type', 'area_square_meter', 'elevator', 'image',]


