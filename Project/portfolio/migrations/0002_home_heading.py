# Generated by Django 3.0.5 on 2020-05-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='heading',
            field=models.TextField(blank=True),
        ),
    ]
