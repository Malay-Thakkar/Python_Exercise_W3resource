# Generated by Django 4.2.11 on 2024-04-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_orderitems_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
