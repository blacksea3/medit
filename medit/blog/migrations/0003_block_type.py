# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_block_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='type',
            field=models.BooleanField(default=False),
        ),
    ]
