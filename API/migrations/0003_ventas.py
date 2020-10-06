# Generated by Django 2.2 on 2020-10-06 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20201005_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaCompra', models.DateField(auto_now_add=True)),
                ('CantidadDeUnidades', models.IntegerField()),
                ('idProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Product')),
                ('idUserrAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.UserAccount')),
            ],
        ),
    ]