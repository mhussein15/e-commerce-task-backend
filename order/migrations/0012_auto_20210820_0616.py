# Generated by Django 3.2.6 on 2021-08-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_order_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='accepted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(blank=True),
        ),
    ]
