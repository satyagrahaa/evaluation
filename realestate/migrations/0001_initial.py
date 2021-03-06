# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('expiration_date', models.DateField(verbose_name='Expiration Date')),
                ('owner', models.CharField(max_length=50, verbose_name='Owner')),
                ('type', models.CharField(choices=[('R', 'Residencial'), ('C', 'Commercial'), ('H', 'House'), ('L', 'Land')], max_length=1, verbose_name='Type')),
                ('image', models.ImageField(upload_to='/media/', verbose_name='Image')),
                ('area_square_meter', models.PositiveIntegerField()),
                ('verification_status', models.CharField(choices=[('V', 'Verified'), ('P', 'Pending'), ('R', 'Rejected')], default='P', max_length=1, verbose_name='Verification Status')),
                ('elevator', models.BooleanField(default=False, verbose_name='Elevator')),
            ],
        ),
    ]
