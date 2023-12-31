# Generated by Django 4.1.3 on 2023-07-18 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=50)),
                ('is_open', models.BooleanField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('profile_image_url', models.CharField(max_length=1000)),
                ('bio', models.CharField(max_length=5000)),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('qtyAvailable', models.IntegerField()),
                ('price', models.IntegerField()),
                ('added_on', models.DateTimeField()),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvcapi.genre')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvcapi.user')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('qty_total', models.IntegerField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvcapi.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvcapi.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mvcapi.user'),
        ),
    ]
