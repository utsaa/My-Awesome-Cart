# Generated by Django 4.0 on 2021-12-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
