# Generated by Django 3.0 on 2020-05-08 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0003_auto_20200423_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='coefficiants',
            field=models.IntegerField(default=1),
        ),
    ]
