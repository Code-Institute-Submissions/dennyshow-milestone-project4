# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-27 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]