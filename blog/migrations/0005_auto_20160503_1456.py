# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
