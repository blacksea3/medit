# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 09:30
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='内容')),
            ],
        ),
    ]
