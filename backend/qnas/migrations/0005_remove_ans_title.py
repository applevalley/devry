# Generated by Django 3.1.5 on 2021-02-08 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qnas', '0004_auto_20210208_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ans',
            name='title',
        ),
    ]
