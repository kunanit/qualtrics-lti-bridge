# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0005_auto_20160524_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ('order',)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='answer',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
    ]