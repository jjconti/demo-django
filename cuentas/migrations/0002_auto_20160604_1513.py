# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='signo',
            field=models.CharField(choices=[('+', '+'), ('-', '-')], max_length=1),
        ),
    ]