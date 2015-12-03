# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0006_auto_20151202_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ownedrecord',
            options={'ordering': ['album']},
        ),
        migrations.AlterUniqueTogether(
            name='ownedrecord',
            unique_together=set([('owner', 'album', 'pressing')]),
        ),
    ]
