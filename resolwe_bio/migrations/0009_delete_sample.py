# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-01 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resolwe_bio', '0008_migrate_sample'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sample',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='sample',
            name='collections',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='contributor',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='data',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='descriptor_schema',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='public_processes',
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
    ]
