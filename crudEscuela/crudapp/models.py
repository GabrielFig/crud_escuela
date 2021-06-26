from django.db import models
from django.utils.regex_helper import Choice

class Admin(models.Model):
    nombre = models.CharField(max_length=50, default='DEFAULT VALUE')
    apellido_paterno = models.CharField(max_length=30, default='DEFAULT VALUE')
    apellido_materno = models.CharField(max_length=30, default='DEFAULT VALUE')
    puesto = models.CharField(max_length=50, default='DEFAULT VALUE')

    class Meta:
         db_table = 'admin'

SEMESTRES = (('1', '1'),
               ('2', '2'),
               ('3', '3'),
               ('4', '4'),
               ('5', '5'),
               ('6', '6'),
               ('7', '7'),
               ('8', '8'),
               ('9', '9'),
               )


class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=30)
    num_cel = models.CharField(max_length=16)
    semestre = models.CharField(max_length=2, choices=SEMESTRES)
    correo = models.EmailField()
    horario_alumno = models.CharField(max_length=30, choices=(('1','Matutino'), ('2','Vespertino')))

    class Meta:
        db_table = 'alumnos'


class Maestro(models.Model):
    nombre =  models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    asignatura = models.CharField(max_length=20)
    horario = models.CharField(max_length=20)

    class Meta:
        db_table = 'maestro'
