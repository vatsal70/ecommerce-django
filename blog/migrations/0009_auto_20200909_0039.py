# Generated by Django 3.0.8 on 2020-09-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200908_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead0',
            new_name='chead3',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='head0',
            new_name='head3',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='blog/images'),
        ),
    ]
