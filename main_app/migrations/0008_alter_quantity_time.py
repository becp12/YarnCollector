# Generated by Django 4.1 on 2022-08-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_quantity_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='time',
            field=models.TimeField(verbose_name='Quantity as of Time'),
        ),
    ]