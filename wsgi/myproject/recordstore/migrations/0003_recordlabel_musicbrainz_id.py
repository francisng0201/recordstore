# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0002_album_musicbrainz_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordlabel',
            name='musicbrainz_id',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
