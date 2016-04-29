# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0002_ewaste'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ngo', models.ForeignKey(to='userside.UserProfile')),
                ('waste', models.ForeignKey(to='userside.Ewaste')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
