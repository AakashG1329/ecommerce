# Generated by Django 5.0.4 on 2024-04-11 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=255)),
                ('status', models.IntegerField(default=1)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField(null=True)),
            ],
            options={
                'db_table': 'tbl_roles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=255, null=True)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField(null=True)),
                ('status', models.IntegerField(default=1)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
            ],
            options={
                'db_table': 'tbl_users',
            },
        ),
    ]
