# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-20 04:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0009_auto_20181119_2137'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='builder',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='builder',
            name='city',
        ),
        migrations.RemoveField(
            model_name='builder',
            name='country',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='builder',
        ),
        migrations.RemoveField(
            model_name='ship',
            name='registers',
        ),
        migrations.DeleteModel(
            name='Builder',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
