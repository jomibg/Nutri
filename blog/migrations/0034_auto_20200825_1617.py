# Generated by Django 3.0.2 on 2020-08-25 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20200822_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.date(2020, 8, 25)),
        ),
    ]
