# Generated by Django 3.2.7 on 2021-10-13 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20211013_1510'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='last_names',
            new_name='last_name',
        ),
    ]
