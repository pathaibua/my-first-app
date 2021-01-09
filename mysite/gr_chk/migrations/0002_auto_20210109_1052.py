# Generated by Django 3.1.4 on 2021-01-09 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gr_chk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boq',
            name='con_val',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='boq',
            name='price_a',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='boq',
            name='price_b',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='boq',
            name='price_c',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='boq',
            name='unit_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]