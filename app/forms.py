from django import forms
from .models import Location
from django.forms import ModelForm, fields


class findLocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        labels = {
            'place': ''
        }
