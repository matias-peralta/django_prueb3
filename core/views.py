from django.http import request
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def Agregar_Obra(request):
    return render(request,'core/Agregar_Obra.html')

def Artistas(request):
    return render(request,'core/Artistas.html')