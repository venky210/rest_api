# Generated by Django 5.0.4 on 2024-04-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0013_customuser_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
