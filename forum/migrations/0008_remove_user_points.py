# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20150915_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='points',
        ),
    ]
