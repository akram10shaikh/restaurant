# Generated by Django 5.1.1 on 2024-10-28 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantname',
            name='verify',
            field=models.CharField(max_length=100, null=True),
        ),
    ]