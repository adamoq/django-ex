# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-21 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0020_auto_20190121_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitertask',
            name='table',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
