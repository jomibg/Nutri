# Generated by Django 3.0.2 on 2020-07-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200729_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]