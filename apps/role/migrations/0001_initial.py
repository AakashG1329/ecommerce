# Generated by Django 5.0.6 on 2024-05-10 09:28

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
    ]
