# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-18 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookConferenceRoomApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='room',
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ManyToManyField(to='BookConferenceRoomApp.Room'),
        ),
    ]