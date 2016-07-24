# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-23 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('engine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='value',
            name='course',
        ),
        migrations.RemoveField(
            model_name='value',
            name='mooclet',
        ),
        migrations.RemoveField(
            model_name='value',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='value',
            name='version',
        ),
        migrations.AddField(
            model_name='value',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='value',
            name='object_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]