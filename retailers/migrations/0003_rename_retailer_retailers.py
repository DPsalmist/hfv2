# Generated by Django 3.2 on 2023-03-31 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retailers', '0002_retailer_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Retailer',
            new_name='Retailers',
        ),
    ]