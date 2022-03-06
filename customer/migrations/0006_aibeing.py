# Generated by Django 3.2.6 on 2021-11-14 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_order_url_hex'),
    ]

    operations = [
        migrations.CreateModel(
            name='aibeing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateField()),
                ('payment', models.BigIntegerField()),
                ('Entry_date', models.DateField()),
                ('order_id', models.TextField()),
                ('payment_id', models.TextField()),
                ('payment_signature_id', models.TextField()),
                ('last_change', models.DateTimeField()),
            ],
        ),
    ]
