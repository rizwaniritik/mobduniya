# Generated by Django 3.0.4 on 2021-09-21 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210921_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email_verified',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_seller',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_no_verified',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
