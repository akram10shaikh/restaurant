# Generated by Django 5.1.1 on 2024-11-23 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_rename_restaurantoff_restaurantname_resturantoff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='resturant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resturant_name', to='myapp.restaurantname'),
        ),
    ]