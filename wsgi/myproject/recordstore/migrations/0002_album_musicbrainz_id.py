# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='musicbrainz_id',
            field=models.CharField(default=b'', max_length=255, null=True),
        ),
    ]
