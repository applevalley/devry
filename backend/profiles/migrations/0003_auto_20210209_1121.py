# Generated by Django 3.1.5 on 2021-02-09 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210208_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joined',
            field=models.DateField(blank=True),
        ),
    ]
