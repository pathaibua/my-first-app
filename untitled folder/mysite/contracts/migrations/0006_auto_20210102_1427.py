# Generated by Django 3.1.4 on 2021-01-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_auto_20210102_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='route_dma',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_no',
            field=models.CharField(max_length=2),
        ),
    ]
