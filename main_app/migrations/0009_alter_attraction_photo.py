# Generated by Django 5.0.4 on 2024-04-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_attraction_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='photo',
            field=models.CharField(),
        ),
    ]