# Generated by Django 4.1.3 on 2023-07-19 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mvcapi', '0003_alter_orderproduct_order_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvcapi.order'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvcapi.product'),
        ),
    ]
