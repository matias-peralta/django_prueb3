# Generated by Django 3.2.5 on 2021-07-11 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('nombre_Artista', models.CharField(max_length=50, verbose_name='nombre del artista')),
                ('edad_Artista', models.IntegerField(verbose_name='Edad')),
                ('nacimiento_Artista', models.CharField(max_length=50, verbose_name='Nacimiento')),
                ('tecnica_Artista', models.CharField(max_length=40, verbose_name='Tecnica')),
                ('descripcion_Artista', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('id_Artista', models.AutoField(primary_key=True, serialize=False, verbose_name='id Artista')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre_usuario', models.CharField(max_length=15, verbose_name='nombre de Usuario')),
                ('clave_usuario', models.CharField(max_length=10, verbose_name='Contraseña')),
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='id Usuario')),
                ('telefono_usuario', models.CharField(max_length=10, verbose_name='Telefono Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='obras',
            fields=[
                ('id_obra', models.AutoField(primary_key=True, serialize=False, verbose_name='id de la obra')),
                ('titulo_obra', models.CharField(max_length=30, verbose_name='titulo de la obra')),
                ('precio_obra', models.IntegerField(verbose_name='precio de la obra')),
                ('tecnica_obra', models.CharField(max_length=30, verbose_name='tecnica de la obra')),
                ('dimenciones_obra', models.IntegerField(verbose_name='dimenciones de la obra')),
                ('peso_obra', models.IntegerField(verbose_name='peso de la obra')),
                ('descripcion_obra', models.CharField(max_length=100, verbose_name='descripcion de la obra')),
                ('imagen_obra', models.CharField(max_length=200, verbose_name='link de la obra')),
                ('Artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artista')),
            ],
        ),
    ]
