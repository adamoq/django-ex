# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-25 17:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0002_auto_20181125_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waiterorder',
            name='currency',
        ),
    ]