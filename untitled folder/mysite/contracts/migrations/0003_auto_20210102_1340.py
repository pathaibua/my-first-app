# Generated by Django 3.1.4 on 2021-01-02 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_auto_20210102_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contract',
            name='po',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='contract',
            name='pr',
            field=models.CharField(default='', max_length=10),
        ),
    ]
