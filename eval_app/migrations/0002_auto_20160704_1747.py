# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 13:17
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eval_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='employee_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='img',
        ),
        migrations.AddField(
            model_name='attribute',
            name='creativity',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10, 'Enter value between 0-10')]),
        ),
        migrations.AddField(
            model_name='attribute',
            name='discipline',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10, 'Enter value between 0-10')]),
        ),
        migrations.AddField(
            model_name='attribute',
            name='employee',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='eval_app.Employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attribute',
            name='overall',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='attribute',
            name='spirit',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10, 'Enter value between 0-10')]),
        ),
        migrations.AddField(
            model_name='attribute',
            name='teamwork',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10, 'Enter value between 0-10')]),
        ),
    ]
