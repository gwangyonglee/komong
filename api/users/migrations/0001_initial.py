# Generated by Django 2.1.7 on 2019-04-28 10:29

import api.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email address')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('last_login_at', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('current_login_at', models.DateTimeField(blank=True, null=True, verbose_name='current login')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
                'ordering': ['-id'],
            },
            managers=[
                ('objects', api.users.models.UserManager()),
            ],
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['created_at'], name='idx_users_created_at'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['username'], name='idx_users_username'),
        ),
    ]