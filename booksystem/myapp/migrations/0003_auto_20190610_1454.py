# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-06-10 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190610_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='epic',
            field=models.ImageField(upload_to='img'),
        ),
    ]
