# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-02 11:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0012_auto_20190102_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='product',
            order_with_respect_to=None,
        ),
    ]