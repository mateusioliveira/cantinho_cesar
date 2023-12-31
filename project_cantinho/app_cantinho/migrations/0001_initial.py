# Generated by Django 4.2.5 on 2023-09-30 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendinha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('products', models.ManyToManyField(to='app_cantinho.product')),
                
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('products_cart', models.ManyToManyField(to='app_cantinho.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('products', models.ManyToManyField(to='app_cantinho.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cantinho.user')),
            ],
        ),
    ]
