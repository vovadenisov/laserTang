# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Category', verbose_name='\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.CharField(max_length=400, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443'),
        ),
    ]
