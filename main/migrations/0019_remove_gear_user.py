# Generated by Django 4.1.5 on 2023-02-12 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_gear_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gear',
            name='user',
        ),
    ]
