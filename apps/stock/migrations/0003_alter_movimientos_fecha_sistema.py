# Generated by Django 4.1.7 on 2023-04-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_rename_operaciones_movimientos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientos',
            name='fecha_sistema',
            field=models.DateField(auto_now=True),
        ),
    ]
