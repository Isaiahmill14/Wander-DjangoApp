# Generated by Django 5.0.3 on 2024-04-10 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_attraction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='location',
            new_name='attraction',
        ),
    ]
