# Generated by Django 5.0.4 on 2024-04-25 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0012_category_product_status_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='admin',
            field=models.BooleanField(default=True),
        ),
    ]
