# Generated by Django 3.2.4 on 2021-06-26 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0007_auto_20210626_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='horario_alumno',
            field=models.CharField(choices=[('1', 'Matutino'), ('2', 'Vespertino')], max_length=30),
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='semestre',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], max_length=2),
        ),
    ]
