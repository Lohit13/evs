# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ECOM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('address', models.CharField(max_length=500, null=True, blank=True)),
                ('phno', models.CharField(max_length=10, null=True, blank=True)),
                ('cname', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
