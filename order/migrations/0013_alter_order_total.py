# Generated by Django 3.2.6 on 2021-08-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20210820_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
