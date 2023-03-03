# Generated by Django 4.1.5 on 2023-03-03 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOdonto', '0010_rename_nombre_servicio_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='apellido',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='apellido',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='especialidad',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='nombre',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='especialidad',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='servicio',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='turno',
            name='paciente',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='turno',
            name='profesional',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='turno',
            name='servicio',
            field=models.CharField(max_length=25),
        ),
    ]
