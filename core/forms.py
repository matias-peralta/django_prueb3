from django import forms
from django.forms import ModelForm, fields, models
from .models import obras

class obrasForm(ModelForm):
    class Meta:
        models = obras
        fields = ['titulo_obra','precio_obra','tecnica_obra','dimenciones_obra','peso_obra','descripcion_obra','imagen_obra']
