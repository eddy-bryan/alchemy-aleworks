# Generated by Django 4.2.13 on 2024-07-08 18:19

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_original_bag_order_stripe_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
