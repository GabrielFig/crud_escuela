from django.db import models

class Admin(models.Model):
    nombre = models.CharField(max_length=50, default='DEFAULT VALUE')
    apellido_paterno = models.CharField(max_length=30, default='DEFAULT VALUE')
    apellido_materno = models.CharField(max_length=30, default='DEFAULT VALUE')
    puesto = models.CharField(max_length=50, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'admin'


class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=30)
    num_cel = models.CharField(max_length=16)
    semestre = models.IntegerField()
    correo = models.EmailField()
    horario_alumno = models.CharField(max_length=30)

    class Meta:
        db_table = 'alumnos'


class Maestro(models.Model):
    nombre =  models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    asignatura = models.CharField(max_length=20)
    img = models.FileField()
    horario = models.CharField(max_length=20)

    class Meta:
        db_table = 'maestro'
