# Generated by Django 3.1.5 on 2021-02-09 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qnas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ans',
            name='title',
        ),
        migrations.AddField(
            model_name='ans',
            name='img',
            field=models.ImageField(default='', upload_to='%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='qna',
            name='img',
            field=models.ImageField(default='', upload_to='%Y/%m/%d'),
        ),
    ]