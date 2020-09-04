# Generated by Django 3.0.2 on 2020-09-02 13:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0045_auto_20200902_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-published_date']},
        ),
        migrations.RemoveIndex(
            model_name='post',
            name='blog_post_publish_a3f863_idx',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 2, 13, 35, 55, 712156, tzinfo=utc)),
        ),
    ]