# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bought_on',
        ),
        migrations.AddField(
            model_name='product',
            name='points',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
