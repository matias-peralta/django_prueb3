from django.urls import path
from .views import Agregar_Obra, home

urlpatterns = [
    path('',home,name="home"),
    path('Agregar_Obras/',Agregar_Obra,name="Agregar_Obra")
]