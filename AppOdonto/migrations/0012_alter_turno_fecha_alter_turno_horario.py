# Generated by Django 4.1.5 on 2023-03-07 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppOdonto', '0011_alter_paciente_apellido_alter_paciente_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='fecha',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='turno',
            name='horario',
            field=models.CharField(max_length=10),
        ),
    ]
