# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-02-02 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0006_language_ab'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
