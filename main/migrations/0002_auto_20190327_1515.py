# Generated by Django 2.1.7 on 2019-03-27 14:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grammar',
            name='grammar_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 14, 15, 53, 702859, tzinfo=utc), verbose_name='Date submitted'),
        ),
    ]
