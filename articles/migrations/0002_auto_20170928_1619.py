# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='articleContent',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='articles',
            name='articleTitle',
            field=models.TextField(max_length=20),
        ),
    ]