from django.urls import path
from .views import Agregar_Obra, Artistas, Conocenos, Crud_Mod_Obra, Crud_del_Obra, Crud_obra, Mod_Obra_Admin, home, Login, Nuevas_Obras, obras_locales, registro

urlpatterns = [
    path('',home,name="home"),
    path('Agregar_Obras/',Agregar_Obra,name="Agregar_Obra"),
    path('Artistas/',Artistas,name="Artistas"),
    path('Conocenos/',Conocenos,name="Conocenos"),
    path('Login/',Login,name="Login"),
    path('Nuevas_Obras/',Nuevas_Obras,name="Nuevas_Obras"),
    path('registro/',registro,name="registro"),
    path('obras_locales/',obras_locales,name="obras_locales"),
    path('Crud_obra',Crud_obra,name="Crud_obra"),
    path('Crud_Mod_Obra/<id>',Crud_Mod_Obra,name="Crud_Mod_Obra"),
    path('Mod_Obra_Admin',Mod_Obra_Admin,name="Mod_Obra_Admin"),
    path('Crud_del_Obra/<id>',Crud_del_Obra,name="Crud_del_Obra"),
    
]