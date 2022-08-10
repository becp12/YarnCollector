# Generated by Django 4.1 on 2022-08-09 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('unit', models.CharField(choices=[('B', 'Ball'), ('S', 'Skein'), ('G', 'Grams'), ('O', 'Ounces')], default='B', max_length=1)),
                ('yarn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.yarn')),
            ],
        ),
    ]
