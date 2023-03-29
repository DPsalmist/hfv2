# Generated by Django 3.2 on 2023-02-27 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignCylinder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cylinder_status', models.CharField(blank=True, default='assigned', max_length=20)),
                ('smart_scale', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SmartDevice',
            fields=[
                ('scale_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('meter_type', models.CharField(blank=True, choices=[('please select', 'please select'), ('smart scale', 'smart scale'), ('smart box', 'smart box')], default='please select', max_length=20)),
                ('manufacturer', models.CharField(default='Homefort Energy', max_length=100)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SmartBox',
        ),
        migrations.DeleteModel(
            name='SmartScale',
        ),
        migrations.AlterField(
            model_name='cylinder',
            name='cylinder_type',
            field=models.CharField(blank=True, choices=[('12kg', '12kg'), ('25kg', '25kg'), ('50kg', '50kg')], max_length=20),
        ),
        migrations.AddField(
            model_name='assigncylinder',
            name='cylinder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.cylinder'),
        ),
        migrations.AddField(
            model_name='assigncylinder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assign', to=settings.AUTH_USER_MODEL),
        ),
    ]
