# Generated by Django 3.1.5 on 2021-02-09 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210209_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joined',
            field=models.DateTimeField(blank=True),
        ),
    ]