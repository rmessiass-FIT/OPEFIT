# Generated by Django 3.2 on 2021-04-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210417_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='clienteorigem',
            name='cliente_id',
            field=models.IntegerField(null=True, verbose_name='Id do Cliente'),
        ),
        migrations.AddField(
            model_name='pedidoorigem',
            name='pedido_id',
            field=models.IntegerField(null=True, verbose_name='Id do Pedido'),
        ),
    ]
