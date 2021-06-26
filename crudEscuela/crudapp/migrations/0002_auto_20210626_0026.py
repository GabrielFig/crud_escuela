# Generated by Django 3.2.4 on 2021-06-26 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apellido_materno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='apellido_paterno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='direccion',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='fecha_nac',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='maestro',
            name='apellido_materno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='maestro',
            name='apellido_paterno',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='maestro',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]