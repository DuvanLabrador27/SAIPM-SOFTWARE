# Generated by Django 2.2.13 on 2022-06-25 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_auto_20220625_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('categoriaId', models.CharField(choices=[('1', 'CC'), ('2', 'Pasa Porte')], max_length=20)),
                ('idUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=40)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('clienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Cliente')),
            ],
            options={
                'verbose_name': 'Cotizacion',
                'verbose_name_plural': 'Cotizacion',
                'db_table': 'cotizacion',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='tamanio',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('clienteId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Cliente')),
                ('cotizacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Cotizacion')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'db_table': 'factura',
            },
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('facturaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Factura')),
                ('productoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto')),
            ],
        ),
    ]
