# Generated by Django 4.1.5 on 2023-02-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_gear_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='gear',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]