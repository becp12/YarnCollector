# Generated by Django 4.1 on 2022-08-10 04:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='amount',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Amount of Yarn left'),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='date',
            field=models.DateField(verbose_name='Quantity as of Date'),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='unit',
            field=models.CharField(choices=[('B', 'Ball'), ('S', 'Skein'), ('G', 'Grams'), ('O', 'Ounces')], default='B', max_length=1, verbose_name='Unit of Measurement'),
        ),
    ]