# Generated by Django 3.1.4 on 2021-01-09 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gr_chk', '0002_auto_20210109_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='gr_chk.contract'),
        ),
    ]
