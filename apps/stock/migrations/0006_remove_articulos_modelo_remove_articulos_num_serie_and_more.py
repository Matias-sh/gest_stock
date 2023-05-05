# Generated by Django 4.1.7 on 2023-05-04 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_rename_id_articulo_movimientos_cod_articulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulos',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='num_serie',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='stock',
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id_stock', models.AutoField(primary_key=True, serialize=False)),
                ('num_serie', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('cantidad', models.PositiveIntegerField()),
                ('cod_articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.articulos')),
            ],
        ),
    ]