# Generated by Django 3.2 on 2023-03-10 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_readings', '0002_auto_20230310_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartboxreadings',
            name='weight',
            field=models.FloatField(max_length=10, null=True),
        ),
    ]
