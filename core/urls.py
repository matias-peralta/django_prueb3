from django.urls import path
from .views import Agregar_Obra, Artistas, Conocenos, home, Login, Nuevas_Obras, registro, Revisar_Obras
#from django.contrib.auth import login
urlpatterns = [
    path('',home,name="home"),
    path('Agregar_Obras/',Agregar_Obra,name="Agregar_Obra"),
    path('Artistas/',Artistas,name="Artistas"),
    path('Conocenos/',Conocenos,name="Conocenos"),
    path('Login/',Login,name="Login"),
    path('Nuevas_Obras/',Nuevas_Obras,name="Nuevas_Obras"),
    path('registro/',registro,name="registro"),
    path('Revisar_Obras/',Revisar_Obras,name="Revisar_Obras"),
    #path(r'^accounts/login/$',  login),

 
]
