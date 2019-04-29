# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 08:51

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resolwe_bio', '0002_sample_presample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='descriptor',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='sample',
            name='settings',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
