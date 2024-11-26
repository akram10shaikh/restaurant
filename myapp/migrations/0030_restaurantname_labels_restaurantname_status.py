# Generated by Django 5.1.1 on 2024-11-14 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0029_alter_termsandconditions_faq_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantname',
            name='labels',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name='restaurantname',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]