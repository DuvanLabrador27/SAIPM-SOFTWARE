# Generated by Django 2.2.13 on 2022-06-25 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_auto_20220625_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='idUsuario',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='idUsuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='factura',
            name='idUsuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
