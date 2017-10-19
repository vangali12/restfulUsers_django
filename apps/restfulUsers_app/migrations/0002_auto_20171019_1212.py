# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restfulUsers_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='smith', max_length=255),
            preserve_default=False,
        ),
    ]