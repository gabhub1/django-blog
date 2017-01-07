# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161222_1132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-name']},
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(help_text='URL name for post', max_length=110, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag_list',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to='blog.Tag'),
        ),
    ]