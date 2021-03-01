# Generated by Django 3.1.7 on 2021-03-01 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210301_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자'),
        ),
    ]
