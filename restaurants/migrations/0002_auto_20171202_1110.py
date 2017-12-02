# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-02 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='Country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='StateOrProvince',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='Telephone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='ZipCode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='city',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='street',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]