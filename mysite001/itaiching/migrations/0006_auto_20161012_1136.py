# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itaiching', '0005_auto_20161012_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='taichiset',
            name='mynote',
            field=models.CharField(default='.', max_length=600, verbose_name='我的筆記'),
        ),
        migrations.AlterField(
            model_name='taichimove',
            name='mynote',
            field=models.CharField(default='.', max_length=600, verbose_name='我的筆記'),
        ),
    ]
