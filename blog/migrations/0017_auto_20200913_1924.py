# Generated by Django 3.0.8 on 2020-09-13 13:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200913_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 9, 13, 13, 54, 42, 351023, tzinfo=utc)),
        ),
    ]