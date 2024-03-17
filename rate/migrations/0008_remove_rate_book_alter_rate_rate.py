# Generated by Django 5.0.3 on 2024-03-13 19:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0007_alter_rate_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='book',
        ),
        migrations.AlterField(
            model_name='rate',
            name='rate',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
