# Generated by Django 4.1 on 2022-08-08 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yarn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]
