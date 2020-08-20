# Generated by Django 3.1 on 2020-08-20 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200820_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='machines_taken',
            field=models.PositiveIntegerField(default=0, verbose_name='Máquinas obtenidas'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='service_taken',
            field=models.PositiveIntegerField(default=0, verbose_name='Servicios tomados'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, help_text='Set to true when the user is a an admin', verbose_name='Es Administrador'),
        ),
    ]