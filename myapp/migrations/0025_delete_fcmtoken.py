# Generated by Django 5.1.1 on 2024-11-12 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_fcmtoken_device_alter_fcmtoken_platform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FCMToken',
        ),
    ]