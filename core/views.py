from django.contrib.auth import authenticate
import core
from core import forms
from core.forms import artistaForm, obrasForm, RegistroForm , AutenticarForm
from core.models import Artista, obras
from django.http import request
from django.shortcuts import render,redirect


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
#lista las obras en mod_obra_admin
def Mod_Obra_Admin(request):
    mobras=obras.objects.all()
    datos={
        'listaobras':mobras
    }
    return render(request,'core/Mod_Obra_Admin.html',datos)
#listar obra en obras_locales
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


def Crud_Mod_Obra(request,id):
    obra = obras.objects.get(id_obra=id)
    datos= {
        'form':obrasForm(instance=obra)
    }
    if request.method == 'POST':
        formulario = obrasForm(data=request.POST, instance=obra)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"

    return render(request,'core/Crud_Mod_Obra.html',datos)

def Crud_del_Obra(request,id):
    obra = obras.objects.get(id_obra = id)
    obra.delete()

    return redirect(to="Mod_Obra_Admin")


def Mod_Artista(request):
    martista=Artista.objects.all()
    datos={
        'listaArtista':martista
    }
    return render(request,'core/Mod_Artista.html',datos)
    
def Agregar_Artista(request):
    datos= {
        'form':artistaForm()
    }
    if request.method == 'POST':
        formulario =artistaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] ="Guardado Correctamente"
    return render(request,'core/Agregar_Artista.html',datos)

def Crud_Mod_Artista(request,id):
    Artista1 = Artista.objects.get(id_Artista=id)
    datos= {
        'form':artistaForm(instance=Artista1)
    }
    if request.method == 'POST':
        formulario = artistaForm(data=request.POST, instance=Artista1)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"

    return render(request,'core/Crud_Mod_Artista.html',datos)

def Crud_del_Artista(request,id):
    Artista1 = Artista.objects.get(id_Artista = id)
    Artista1.delete()

    return redirect(to="Mod_Artista")

#cracion del login
def login (request):
    form = AutenticarForm()
    return render(request, "core/login.html", {'form':form})

def registro(request):
    form = RegistroForm()
    return render(request, "core/registro.html", {'form':form})
