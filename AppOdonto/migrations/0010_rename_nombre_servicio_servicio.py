# Generated by Django 4.1.5 on 2023-03-02 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppOdonto', '0009_rename_user_avatar_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='nombre',
            new_name='servicio',
        ),
    ]