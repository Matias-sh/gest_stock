# Generated by Django 4.1.7 on 2023-04-14 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Operaciones',
            new_name='Movimientos',
        ),
        migrations.RenameModel(
            old_name='Tpo_Operaciones',
            new_name='Tpo_Movimientos',
        ),
        migrations.RenameField(
            model_name='movimientos',
            old_name='id_operacion',
            new_name='id_movimiento',
        ),
        migrations.RenameField(
            model_name='tpo_movimientos',
            old_name='id_tpo_operacion',
            new_name='id_tpo_movimiento',
        ),
    ]