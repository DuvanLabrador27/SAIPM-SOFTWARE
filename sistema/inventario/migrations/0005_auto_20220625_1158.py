# Generated by Django 2.2.13 on 2022-06-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20220625_1151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallefactura',
            options={'verbose_name': 'FacturaDetalle', 'verbose_name_plural': 'FacturasDetalles'},
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterModelTable(
            name='detallefactura',
            table='facturaDetalle',
        ),
    ]
