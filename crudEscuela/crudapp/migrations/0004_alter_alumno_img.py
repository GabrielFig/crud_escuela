# Generated by Django 3.2.4 on 2021-06-26 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_alter_alumno_num_cel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='img',
            field=models.FileField(default='', null=True, upload_to=''),
        ),
    ]