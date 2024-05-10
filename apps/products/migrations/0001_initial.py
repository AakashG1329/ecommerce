# Generated by Django 5.0.6 on 2024-05-10 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('height', models.IntegerField(null=True)),
                ('width', models.IntegerField(null=True)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField(null=True)),
                ('status', models.IntegerField(default=1)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
            options={
                'db_table': 'tbl_products',
            },
        ),
    ]