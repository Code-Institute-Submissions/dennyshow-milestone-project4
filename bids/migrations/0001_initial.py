# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-27 17:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auctions', '0002_auto_20191127_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_time', models.DateTimeField(blank=True, default='', null=True)),
                ('auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Auction')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]