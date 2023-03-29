# Generated by Django 3.2 on 2023-03-08 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0007_remove_assigncylinder_cylinder'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assigncylinder',
            options={'ordering': ('-assigned_date',)},
        ),
        migrations.RenameField(
            model_name='assigncylinder',
            old_name='date_assigned',
            new_name='assigned_date',
        ),
        migrations.AddField(
            model_name='assigncylinder',
            name='cylinder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.cylinder'),
        ),
    ]
