# Generated by Django 3.0.2 on 2020-08-22 19:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_auto_20200822_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.DeleteModel(
            name='Additional_link',
        ),
    ]