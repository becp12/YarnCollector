# Generated by Django 4.1 on 2022-08-10 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_quantity_amount_alter_quantity_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quantity',
            options={'ordering': ['-date']},
        ),
    ]
