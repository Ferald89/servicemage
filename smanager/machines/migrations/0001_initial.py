# Generated by Django 3.0.9 on 2020-08-03 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='DateTime on wich the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='DateTime on wich the object was last modiefed', verbose_name='modified at')),
                ('name', models.CharField(max_length=140, verbose_name='project name')),
                ('serial_number', models.SlugField(max_length=140, unique=True)),
                ('model', models.CharField(max_length=140, verbose_name='model')),
                ('about', models.CharField(max_length=255, verbose_name='machine description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='machine/picture')),
                ('next_service', models.DateTimeField()),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='DateTime on wich the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='DateTime on wich the object was last modiefed', verbose_name='modified at')),
                ('is_active', models.BooleanField(default=True, help_text='Only active user ar allowed to interact with the machine', verbose_name='active status')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machines.Machine')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]