# Generated by Django 4.1 on 2022-09-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='identification',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='identification',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
