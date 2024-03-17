# Generated by Django 5.0.3 on 2024-03-17 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0007_alter_publisher_certificate'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='book/')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('language', models.CharField(choices=[('Arabic', 'Arabic'), ('English', 'English'), ('French', 'French')], max_length=7)),
                ('no_of_page', models.IntegerField()),
                ('year_of_publication', models.DateField()),
                ('total_number_of_book', models.IntegerField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_author', to='account.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publisher_book', to='users.custompublisher')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_category', to='book.category')),
            ],
        ),
    ]
