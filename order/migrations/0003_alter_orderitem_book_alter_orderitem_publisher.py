# Generated by Django 5.0.3 on 2024-03-21 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_initial'),
        ('order', '0002_alter_cartitem_cart'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_book_item', to='book.book'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_publisher_item', to='users.custompublisher'),
        ),
    ]
