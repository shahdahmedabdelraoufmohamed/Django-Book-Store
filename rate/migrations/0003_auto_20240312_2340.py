# Generated by Django 2.2.28 on 2024-03-12 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0002_alter_rate_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]