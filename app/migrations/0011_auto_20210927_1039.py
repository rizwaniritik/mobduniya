# Generated by Django 3.0.4 on 2021-09-27 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210926_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='customer_image',
            field=models.ImageField(upload_to='productimg'),
        ),
    ]
