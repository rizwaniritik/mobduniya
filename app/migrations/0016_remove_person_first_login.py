# Generated by Django 3.0.4 on 2021-10-19 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20211019_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='first_login',
        ),
    ]