from django import forms
from django.forms import ModelForm, fields
from .models import obras

class obrasForm(ModelForm):
    class Meta:
        model = obras
        fields = ['titulo_obra','precio_obra','tecnica_obra','dimenciones_obra','peso_obra','descripcion_obra','imagen_obra']
