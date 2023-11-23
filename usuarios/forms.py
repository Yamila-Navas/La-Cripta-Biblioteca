from django import forms
from django.forms import ModelForm
from .models import Usuarios, Prestamos, Colección


class Usuario_Form(ModelForm):
    class Meta:
        model = Usuarios
        exclude = ('fecha_de_registro','historial_de_prestamos',)
        widgets = {
            'adeuda': forms.HiddenInput(),
        }


class Prestamos_Form(ModelForm):
    class Meta:
        model = Prestamos
        exclude = ('fecha_de_prestamo',)
        widgets = {
            'fecha_de_devolucion': forms.DateInput(attrs={'type': 'date'}),
            'usuario': forms.HiddenInput(),
            'devuelto': forms.HiddenInput(),
        }

    libros = forms.ModelMultipleChoiceField(
        queryset=Colección.objects.filter(disponible=True),
        widget=forms.SelectMultiple(attrs={
            'data-searchable': 'true',
            'data-ajax--url': '/usuarios/buscar_libros/',
        })
    )

    





