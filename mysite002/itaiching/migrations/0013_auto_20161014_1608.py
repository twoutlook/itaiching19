# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itaiching', '0012_auto_20161014_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taichimove',
            name='setnum',
            field=models.IntegerField(default=12, verbose_name='第幾式'),
        ),
        migrations.AlterField(
            model_name='taichimove',
            name='stylenum',
            field=models.IntegerField(default=38, verbose_name='幾式'),
        ),
    ]
