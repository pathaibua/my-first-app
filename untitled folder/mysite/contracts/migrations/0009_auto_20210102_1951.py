# Generated by Django 3.1.4 on 2021-01-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0008_route_route_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contract_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_no',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
