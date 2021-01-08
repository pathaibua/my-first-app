# Generated by Django 3.1.4 on 2021-01-02 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_auto_20210102_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_no', models.CharField(max_length=200)),
                ('route_name', models.CharField(max_length=200)),
                ('route_level', models.CharField(max_length=1)),
                ('price_E', models.DecimalField(decimal_places=4, max_digits=19)),
                ('price_W', models.DecimalField(decimal_places=4, max_digits=19)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.contract')),
            ],
        ),
    ]
