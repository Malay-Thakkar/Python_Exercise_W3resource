# Generated by Django 4.2.11 on 2024-04-05 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_rename_user_customuser_shipping_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='shipping_address',
            new_name='shipping_address_model',
        ),
    ]
