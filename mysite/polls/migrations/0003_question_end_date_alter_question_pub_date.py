# Generated by Django 4.0.1 on 2022-01-24 12:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_choise_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 12, 3, 55, 88891, tzinfo=utc), verbose_name='ending date'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 12, 3, 55, 88891, tzinfo=utc), verbose_name='date published'),
        ),
    ]
