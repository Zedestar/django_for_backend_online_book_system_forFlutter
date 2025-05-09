# Generated by Django 5.1.6 on 2025-02-18 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='picture_images')),
                ('preview', models.FileField(upload_to='book_previews')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.author')),
                ('Publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.publisher')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.subject')),
            ],
        ),
    ]
