# Generated by Django 4.0.6 on 2022-08-03 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_customer_order_product_shippingaddress_orderitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='abouttxt',
            field=models.TextField(default=''),
        ),
    ]