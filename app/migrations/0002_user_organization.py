# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.IntegerField(null=True),
        ),
    ]