# Generated by Django 3.2.15 on 2022-10-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0004_auto_20221017_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='mprofile',
            name='address',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='mprofile',
            name='age',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='mprofile',
            name='birthday',
            field=models.DateTimeField(default=None, max_length=100),
        ),
    ]
