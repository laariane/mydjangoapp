# Generated by Django 3.0 on 2020-05-08 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0004_module_coefficiants'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='edtudiant',
            field=models.ManyToManyField(to='administrateur.Etudiant'),
        ),
    ]
