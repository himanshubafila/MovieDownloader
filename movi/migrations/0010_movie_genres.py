# Generated by Django 3.0.5 on 2020-06-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movi', '0009_remove_movie_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
