# Generated by Django 3.1.2 on 2020-10-09 21:40

import API.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=API.models.upload_path),
        ),
    ]
