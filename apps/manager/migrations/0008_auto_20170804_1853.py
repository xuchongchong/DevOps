# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_remove_storage_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hosts', to='manager.Group', verbose_name='_Group'),
        ),
        migrations.AlterField(
            model_name='host',
            name='storages',
            field=models.ManyToManyField(blank=True, related_name='hosts', to='manager.Storage', verbose_name='Host storages'),
        ),
    ]