# Generated by Django 5.0.4 on 2024-04-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0021_cart_added_at_wishlist_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='SKU',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
