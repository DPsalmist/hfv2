# Generated by Django 3.2 on 2023-02-27 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_auto_20230227_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigncylinder',
            name='cylinder_status',
        ),
    ]
