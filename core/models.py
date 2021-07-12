from django.db import models


# Create your models here.
class Artista(models.Model):
    nombre_Artista = models.CharField(max_length=50, verbose_name="nombre del artista")
    edad_Artista = models.IntegerField(verbose_name="Edad")
    nacimiento_Artista = models.CharField(max_length=50, verbose_name="Nacimiento")
    tecnica_Artista = models.CharField(max_length=40, verbose_name="Tecnica")
    descripcion_Artista= models.CharField(max_length=200, verbose_name="Descripcion")
    id_Artista = models.AutoField(primary_key=True,verbose_name="id Artista")

    def __str__(self) :
        return self.nombre_Artista

class obras(models.Model):
    id_obra =models.AutoField(primary_key=True,verbose_name="id de la obra")
    titulo_obra=models.CharField(max_length=30,verbose_name="titulo de la obra")
    precio_obra=models.IntegerField(verbose_name="precio de la obra")
    tecnica_obra=models.CharField(max_length=30,verbose_name="tecnica de la obra")
    dimenciones_obra=models.IntegerField(verbose_name="dimenciones de la obra")
    peso_obra=models.IntegerField(verbose_name="peso de la obra")
    descripcion_obra=models.CharField(max_length=100,verbose_name="descripcion de la obra")
    imagen_obra=models.CharField(max_length=200,verbose_name="link de la obra")
    Artista=models.ForeignKey(Artista,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_obra


class Usuario(models.Model):
    nombre_usuario= models.CharField(max_length=15, verbose_name="nombre de Usuario")
    clave_usuario= models.CharField(max_length=10, verbose_name="Contraseña")
    id_usuario = models.AutoField(primary_key=True,verbose_name="id Usuario")
    telefono_usuario= models.CharField(max_length=10, verbose_name="Telefono Usuario")

    def __str__(self) :
        return self.nombre_usuario      