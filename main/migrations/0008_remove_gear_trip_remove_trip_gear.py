# Generated by Django 4.1.5 on 2023-02-11 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_trip_gear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='gear',
        ),
    ]
