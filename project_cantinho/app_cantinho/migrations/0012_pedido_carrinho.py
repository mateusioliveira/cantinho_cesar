# Generated by Django 4.2.5 on 2023-10-28 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_cantinho', '0011_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='carrinho',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_cantinho.cart'),
        ),
    ]
