# Generated by Django 3.1 on 2020-08-27 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('machines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='manual',
            name='used_in',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.machine', verbose_name='Máquina del manual'),
        ),
        migrations.AddField(
            model_name='machine',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Propietario'),
        ),
    ]
