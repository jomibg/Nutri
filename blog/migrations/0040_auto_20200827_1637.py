# Generated by Django 3.0.2 on 2020-08-27 16:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_auto_20200827_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 8, 27, 16, 37, 8, 550756, tzinfo=utc)),
        ),
    ]
