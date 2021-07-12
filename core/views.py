from core.forms import obrasForm
from core.models import obras
from django.http import request
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def Agregar_Obra(request):
    return render(request,'core/Agregar_Obra.html')

def Artistas(request):
    return render(request,'core/Artistas.html')

def Conocenos(request):
    return render(request,'core/Conocenos.html')

def Login(request):
    return render(request,'core/Login.html')

def Nuevas_Obras(request):
    return render(request,'core/Nuevas_Obras.html')

def registro(request):
    return render(request,'core/registro.html')

def obras_locales(request):
    mobras=obras.objects.all()
    datos={
        'listaobras':mobras
    }
    return render(request,'core/obras_locales.html',datos)

def Crud_obra(request):
    datos= {
        'form':obrasForm()
    }
    if request.method == 'POST':
        formulario =obrasForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] ="Guardado Correctamente"
    return render(request,'core/Crud_obra.html',datos)


def Crud_Obra(request,id):
    obra = obras