from django.urls import path
from .views import Agregar_Artista, Agregar_Obra, Artista_Bai_Xaochin, Artista_Ichigo, Artista_Miguel_Works, Artista_Nathan, Artistas, Conocenos, Crud_Mod_Artista, Crud_Mod_Obra, Crud_del_Artista, Crud_del_Obra, Crud_obra, Mod_Artista, Mod_Obra_Admin, home, Login, Nuevas_Obras, obras_locales, registro

urlpatterns = [
    path('',home,name="home"),
    path('Agregar_Obras/',Agregar_Obra,name="Agregar_Obra"),
    path('Artistas/',Artistas,name="Artistas"),
    path('Conocenos/',Conocenos,name="Conocenos"),
    path('Login/',Login,name="Login"),
    path('Nuevas_Obras/',Nuevas_Obras,name="Nuevas_Obras"),
    path('registro/',registro,name="registro"),
    path('obras_locales/',obras_locales,name="obras_locales"),
    #link de los crud de las obras
    path('Crud_obra',Crud_obra,name="Crud_obra"),
    path('Crud_Mod_Obra/<id>',Crud_Mod_Obra,name="Crud_Mod_Obra"),
    path('Mod_Obra_Admin',Mod_Obra_Admin,name="Mod_Obra_Admin"),
    path('Crud_del_Obra/<id>',Crud_del_Obra,name="Crud_del_Obra"),
    #link de loa crus de los artistas
    path('Agregar_Artista',Agregar_Artista,name="Agregar_Artista"),
    path('Crud_Mod_Artista/<id>',Crud_Mod_Artista,name="Crud_Mod_Artista"),
    path('Mod_Artista',Mod_Artista,name="Mod_Artista"),
    path('Crud_del_Artista/<id>',Crud_del_Artista,name="Crud_del_Artista"),
    #paginas interiores
    path('Artista_Ichigo',Artista_Ichigo,name="Artista_Ichigo"),
    path('Artista_Nathan',Artista_Nathan,name="Artista_Nathan"),
    path('Artista_Bai_Xaochin',Artista_Bai_Xaochin,name="Artista_Bai_Xaochin"),
    path('Artista_Miguel_Works',Artista_Miguel_Works,name="Artista_Miguel_Works"),

    
]