# Generated by Django 3.0.2 on 2020-08-10 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200809_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.date(2020, 8, 10)),
        ),
    ]
