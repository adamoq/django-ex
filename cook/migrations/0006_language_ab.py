# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-31 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0005_auto_20190125_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='ab',
            field=models.CharField(max_length=7, null=True),
        ),
    ]