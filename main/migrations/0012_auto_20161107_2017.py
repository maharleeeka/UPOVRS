# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20161026_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentedequipment',
            name='request_id',
            field=models.DecimalField(decimal_places=0, max_digits=4, null=True),
        ),
    ]
