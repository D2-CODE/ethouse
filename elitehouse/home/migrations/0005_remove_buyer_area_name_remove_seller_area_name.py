# Generated by Django 5.0.1 on 2024-02-14 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_buyer_password_employee_password_seller_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='area_name',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='area_name',
        ),
    ]
