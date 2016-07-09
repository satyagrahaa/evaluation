from django import forms

from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'owner', 'type', 'area_square_meter', 'elevator', 'image',]


