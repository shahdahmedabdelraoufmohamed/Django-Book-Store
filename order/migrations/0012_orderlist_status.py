# Generated by Django 4.2.11 on 2024-03-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_orderlist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20),
        ),
    ]
