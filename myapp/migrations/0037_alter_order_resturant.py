# Generated by Django 5.1.1 on 2024-11-23 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0036_alter_order_resturant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='resturant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.restaurantname'),
        ),
    ]
