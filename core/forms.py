from django import forms
from django.forms import ModelForm, fields
from .models import Artista, obras

class obrasForm(ModelForm):
    class Meta:
        model = obras
        fields = ['titulo_obra','precio_obra','tecnica_obra','dimenciones_obra','peso_obra','descripcion_obra','imagen_obra','Artista']

class artistaForm(ModelForm):
    class Meta:
        model = Artista
        fields =['nombre_Artista','edad_Artista','nacimiento_Artista','tecnica_Artista','descripcion_Artista','id_Artista']