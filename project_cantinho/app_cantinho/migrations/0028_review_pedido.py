# Generated by Django 4.2.5 on 2023-11-17 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_cantinho', '0027_remove_review_vendinha'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='pedido',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app_cantinho.pedido'),
        ),
    ]
