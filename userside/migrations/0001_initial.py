# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('isNgo', models.BooleanField(default=False)),
                ('isEcom', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('number', models.CharField(max_length=100, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
