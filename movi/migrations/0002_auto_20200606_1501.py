# Generated by Django 3.0.5 on 2020-06-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.CharField(default=' ', max_length=100000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(default=' ', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='link',
            field=models.CharField(default=' ', max_length=1000000),
        ),
    ]
