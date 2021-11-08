# Generated by Django 3.0.4 on 2021-09-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210921_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='landmark',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='state',
            field=models.CharField(blank=True, choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andra Pradesh', 'Andra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Daman & Diu', 'Daman & Diu'), ('Delhi', 'Delhi'), ('Goa', 'Goa'), ('Gujrat', 'Gujrat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='zipcode',
            field=models.IntegerField(blank=True),
        ),
    ]
