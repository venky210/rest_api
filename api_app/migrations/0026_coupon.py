# Generated by Django 5.0.4 on 2024-04-29 03:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0025_rename_disscount_product_disscount_per'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaild', models.DateTimeField()),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api_app.product')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]