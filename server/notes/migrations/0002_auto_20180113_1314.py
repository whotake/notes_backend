# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=180, verbose_name='Описание'),
        ),
    ]