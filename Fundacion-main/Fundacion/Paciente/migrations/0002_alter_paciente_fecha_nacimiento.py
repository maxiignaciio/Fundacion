# Generated by Django 4.0.5 on 2022-06-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.TextField(max_length=10),
        ),
    ]