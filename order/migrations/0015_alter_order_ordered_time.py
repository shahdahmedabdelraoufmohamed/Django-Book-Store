# Generated by Django 4.2.11 on 2024-04-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_alter_order_ordered_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_time',
            field=models.TimeField(default='05:00:12'),
        ),
    ]
