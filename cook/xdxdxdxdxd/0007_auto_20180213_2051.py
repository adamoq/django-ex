# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0006_auto_20180207_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phonenumber',
            field=models.CharField(max_length=12),
        ),
    ]