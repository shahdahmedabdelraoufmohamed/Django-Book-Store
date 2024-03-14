# Generated by Django 5.0.3 on 2024-03-13 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_remove_book_rates'),
        ('rate', '0006_rate_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_review', to='book.book'),
        ),
    ]
