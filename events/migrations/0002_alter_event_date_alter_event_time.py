# Generated by Django 4.1.7 on 2023-06-12 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
