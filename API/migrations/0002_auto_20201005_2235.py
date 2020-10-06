# Generated by Django 2.2 on 2020-10-06 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='modelo',
            field=models.CharField(choices=[('convencional', 'convencional'), ('cosmeticos', 'cosmeticos'), ('de contacto', 'de contacto')], default='convencional', max_length=30),
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
