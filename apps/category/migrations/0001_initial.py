# Generated by Django 5.0.6 on 2024-05-10 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('displayOrder', models.IntegerField()),
                ('code', models.CharField(max_length=250)),
                ('img_url', models.CharField(max_length=250)),
                ('width', models.IntegerField(null=True)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField(null=True)),
                ('status', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'tbl_categorys',
            },
        ),
    ]
