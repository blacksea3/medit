# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_block_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attach',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('src', models.CharField(max_length=100)),
                ('file_name', models.CharField(max_length=80)),
                ('modifytime', models.DateTimeField(auto_now=True)),
                ('remark', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='attachids',
            field=models.CharField(default='', max_length=20),
        ),
    ]
