# Generated by Django 4.1.5 on 2023-02-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_gear_trip_alter_gear_necessary'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='trip',
            field=models.ManyToManyField(to='main.trip'),
        ),
    ]
