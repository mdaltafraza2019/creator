# Generated by Django 4.2 on 2023-09-23 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_file_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='user',
            new_name='username',
        ),
    ]
