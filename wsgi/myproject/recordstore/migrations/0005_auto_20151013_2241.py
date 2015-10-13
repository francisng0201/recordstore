# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0004_auto_20151013_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='release_format',
        ),
        migrations.AddField(
            model_name='pressing',
            name='release_format',
            field=models.CharField(default=b'', max_length=255, choices=[(b'cd', b'CD'), (b'vinyl_12', b'Vinyl 12 inch'), (b'vinyl_7', b'Vinyl 7 inch'), (b'tape', b'Tape')]),
        ),
    ]
