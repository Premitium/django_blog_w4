# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170316_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='blog.Tag'),
        ),
    ]
