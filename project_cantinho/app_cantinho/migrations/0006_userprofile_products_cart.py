# Generated by Django 4.2.5 on 2023-10-25 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cantinho', '0005_userprofile_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='products_cart',
            field=models.ManyToManyField(to='app_cantinho.product'),
        ),
    ]
