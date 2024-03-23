# Generated by Django 5.0.3 on 2024-03-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.CharField(default='desouk', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(default='Egypt', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='phone',
            field=models.CharField(default='01113283302', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(default='staduim street', max_length=300),
            preserve_default=False,
        ),
    ]