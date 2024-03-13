# Generated by Django 5.0.3 on 2024-03-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_book_language'),
        ('rate', '0005_alter_rate_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rates',
            field=models.ManyToManyField(related_name='books', to='rate.rate'),
        ),
    ]
