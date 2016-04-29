# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0003_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='points',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
