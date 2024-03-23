# Generated by Django 4.2.11 on 2024-03-23 01:36
# Generated by Django 5.0.3 on 2024-03-23 12:43

import creditcards.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=creditcards.models.CardNumberField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expire',
            field=creditcards.models.CardExpiryField(blank=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='security_code',
            field=creditcards.models.SecurityCodeField(blank=True, max_length=4),
        ),
    ]
