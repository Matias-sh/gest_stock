# Generated by Django 4.1.7 on 2023-05-08 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_rename_stock_inventario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='cod_articulo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.articulos'),
        ),
    ]