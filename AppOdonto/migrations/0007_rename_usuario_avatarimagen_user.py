# Generated by Django 4.1.5 on 2023-03-02 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppOdonto', '0006_rename_pacientemodel_paciente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatarimagen',
            old_name='usuario',
            new_name='user',
        ),
    ]