# Generated by Django 4.0.1 on 2022-04-06 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancies',
            old_name='Imagesrs',
            new_name='imagesrs',
        ),
        migrations.RenameField(
            model_name='vacancies',
            old_name='Telephonenumber',
            new_name='telephonenumber',
        ),
    ]
