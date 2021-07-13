from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields
from django.forms.widgets import PasswordInput
from .models import Artista, Usuario, obras
#from django.contrib.auth.forms import authenticate


class RegistroForm(UserCreationForm):
    clave_usuario1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=True)
    clave_usuario2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)

    class Meta:
        model = Usuario
        fields =('telefono_usuario','nombre_usuario','clave_usuario1','clave_usuario2')
        labels = {'nombre_usuario': 'Nombre completo','telefono_usuario': 'ingrese telefono'}

class AutenticarForm(forms.ModelForm):
    clave_usuario =forms.CharField (label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario 
        field =('nombre_usuario', 'clave_usuario')

    def clean(self):
        nombre_usuario = self.cleaned_data['nombre_usuario']
        clave_usuario= self.cleaned_data['clave_usuario']

        if not authenticate(nombre_usuario=nombre_usuario , clave_usuario=clave_usuario):
            raise forms.ValidationError("El nombre de usuario o la contraseña son incorrectos")






class obrasForm(ModelForm):
    class Meta:
        model = obras
        fields = ['titulo_obra','precio_obra','tecnica_obra','dimenciones_obra','peso_obra','descripcion_obra','imagen_obra','Artista']

class artistaForm(ModelForm):
    class Meta:
        model = Artista
        fields =['nombre_Artista','edad_Artista','nacimiento_Artista','tecnica_Artista','descripcion_Artista','id_Artista']