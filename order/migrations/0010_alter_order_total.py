# Generated by Django 3.2.6 on 2021-08-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]