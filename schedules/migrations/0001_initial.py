# Generated by Django 4.1.7 on 2023-06-12 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('scheduleID', models.AutoField(primary_key=True, serialize=False)),
                ('userID', models.IntegerField()),
                ('roomID', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
