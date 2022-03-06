# Generated by Django 3.2.6 on 2021-09-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField()),
                ('total', models.BigIntegerField()),
                ('gst', models.IntegerField()),
                ('after_gst', models.BigIntegerField()),
                ('service_charge', models.IntegerField()),
                ('delivery_charge', models.IntegerField()),
                ('grand_total', models.BigIntegerField()),
                ('customer_id', models.BigIntegerField()),
                ('customer_access', models.TextField()),
                ('cart_status', models.TextField()),
                ('status', models.TextField()),
                ('last_change', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField()),
                ('cart_id', models.BigIntegerField()),
                ('item_id', models.IntegerField()),
                ('item_name', models.TextField()),
                ('item_image', models.TextField()),
                ('quantity', models.IntegerField()),
                ('bef_disc_price', models.BigIntegerField()),
                ('discount', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.TextField()),
                ('last_change', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField()),
                ('cart_id', models.BigIntegerField()),
                ('total', models.BigIntegerField()),
                ('gst', models.IntegerField()),
                ('after_gst', models.BigIntegerField()),
                ('service_charge', models.IntegerField()),
                ('delivery_charge', models.IntegerField()),
                ('grand_total', models.BigIntegerField()),
                ('customer_id', models.BigIntegerField()),
                ('customer_access', models.TextField()),
                ('order_status', models.TextField()),
                ('delivery_type', models.TextField()),
                ('payment_mode', models.TextField()),
                ('arrival_time', models.TimeField()),
                ('payment_id', models.TextField()),
                ('delivery_otp', models.IntegerField()),
                ('confirm_otp', models.IntegerField()),
                ('cancel_reason', models.TextField()),
                ('payment_status', models.TextField()),
                ('status', models.TextField()),
                ('last_change', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='order_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField()),
                ('order_id', models.BigIntegerField()),
                ('item_id', models.IntegerField()),
                ('item_name', models.TextField()),
                ('item_image', models.TextField()),
                ('quantity', models.IntegerField()),
                ('bef_disc_price', models.BigIntegerField()),
                ('discount', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.TextField()),
                ('last_change', models.DateTimeField()),
            ],
        ),
    ]
