# Generated by Django 5.0.1 on 2024-02-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_buyer_area_name_remove_seller_area_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
