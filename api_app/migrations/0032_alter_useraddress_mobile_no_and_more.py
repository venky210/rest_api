# Generated by Django 5.0.4 on 2024-04-29 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0031_payment_useraddress_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='mobile_no',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='pincode',
            field=models.IntegerField(max_length=5),
        ),
    ]
