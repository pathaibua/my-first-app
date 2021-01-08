# Generated by Django 3.1.4 on 2021-01-08 13:00

from django.db import migrations, models
import django.db.models.deletion
import gr_chk.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_name', models.CharField(max_length=50)),
                ('po', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_order', models.IntegerField(default=gr_chk.models.Route.number)),
                ('plan_id', models.CharField(max_length=12)),
                ('route_name', models.CharField(max_length=100)),
                ('route_level', models.CharField(max_length=1)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gr_chk.contract')),
            ],
        ),
        migrations.CreateModel(
            name='boq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_pk', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=50)),
                ('parent', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=200)),
                ('unit_name', models.CharField(max_length=10)),
                ('price_a', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_b', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_c', models.DecimalField(decimal_places=2, max_digits=10)),
                ('con_val', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gr_chk.contract')),
            ],
        ),
    ]
