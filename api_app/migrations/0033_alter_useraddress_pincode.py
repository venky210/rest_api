# Generated by Django 5.0.4 on 2024-04-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0032_alter_useraddress_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='pincode',
            field=models.IntegerField(max_length=6),
        ),
    ]
