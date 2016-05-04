# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=64)),
                ('result', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=8192)),
                ('component_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adaptive_engine_app.Component')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adaptive_engine_app.Version'),
        ),
    ]
