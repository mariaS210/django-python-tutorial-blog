# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-17 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_posttext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttext',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textblock', to='blog.Post'),
        ),
    ]
