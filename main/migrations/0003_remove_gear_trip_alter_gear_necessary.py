# Generated by Django 4.1.5 on 2023-02-11 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_gear'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='trip',
        ),
        migrations.AlterField(
            model_name='gear',
            name='necessary',
            field=models.CharField(max_length=100),
        ),
    ]