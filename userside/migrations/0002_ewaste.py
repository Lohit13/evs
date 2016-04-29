# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import userside.models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ewaste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('bought_on', models.DateTimeField()),
                ('pic', models.FileField(upload_to=userside.models.get_upload_file_name)),
                ('user', models.ForeignKey(to='userside.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
