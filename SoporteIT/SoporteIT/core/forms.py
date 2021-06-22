from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Solicitud, Contratacion

class SolicitudForm(ModelForm):

    class Meta:
        model = Solicitud
        fields =['rut', 'nombre', 'apellido', 'region', 'comuna', 'correo','contratacion', 'comentario']
        labels ={
            'rut': 'rut', 
            'nombre': 'nombre', 
            'apellido': 'apellido', 
            'region': 'region',
            'comuna': 'comuna',
            'correo': 'correo',
            'contratacion': 'contratacion',
            'comentario': 'comentario',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese apellido', 
                    'id': 'apellido'
                }
            ), 
            'region': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese region',
                    'id': 'region',
                }
            ),
            'comuna': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese comuna', 
                    'id': 'comuna'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese correo', 
                    'id': 'correo'
                }
            ),
             'contratacion': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'contratacion',
                }
            ),
            'comentario': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese comentario', 
                    'id': 'comentario'
                }
            ),
            

        }