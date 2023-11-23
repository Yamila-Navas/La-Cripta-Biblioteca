from django import forms
from django.forms import ModelForm
from .models import Colección

class Colección_form(ModelForm):
    class Meta:
        model = Colección
        exclude = ('fecha_de_entrada',)
        widgets = {
            'fecha_de_publicacion': forms.DateInput(attrs={'type': 'date'})
        }
    class Media:
        enctype = 'multipart/form-data'

   