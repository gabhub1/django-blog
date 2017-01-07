# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-30 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20161230_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': 'date_added', 'ordering': ['-date_added', 'title'], 'permissions': (('user_add_his_post', 'User can add his own posts'), ('user_edit_his_post', 'User can edit his own posts'), ('user_remove_his_post', 'User can remove his own posts'))},
        ),
    ]