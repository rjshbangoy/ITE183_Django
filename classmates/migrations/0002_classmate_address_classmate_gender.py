# Generated by Django 4.2.7 on 2023-11-07 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classmate',
            name='address',
            field=models.CharField(default='Address here', max_length=200),
        ),
        migrations.AddField(
            model_name='classmate',
            name='gender',
            field=models.CharField(default='Male/Female', max_length=6),
        ),
    ]
