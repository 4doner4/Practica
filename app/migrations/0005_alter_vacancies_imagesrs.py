# Generated by Django 3.2.12 on 2022-02-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220222_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancies',
            name='Imagesrs',
            field=models.CharField(max_length=50, verbose_name='Imageurl'),
        ),
    ]