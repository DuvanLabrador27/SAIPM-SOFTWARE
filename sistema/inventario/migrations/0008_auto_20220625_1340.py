# Generated by Django 2.2.13 on 2022-06-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_auto_20220625_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='categoriaId',
            field=models.CharField(choices=[('1', 'CC'), ('2', 'PasaPorte')], max_length=20),
        ),
    ]
