# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0003_auto_20151026_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressing',
            name='release_format',
            field=models.CharField(default=b'', max_length=255, choices=[(b'', b'Unknown'), (b'cd', b'CD'), (b'vinyl_12', b'Vinyl - 12 inch'), (b'vinyl_2_12', b'Vinyl - Double LP 12 inch'), (b'vinyl_10', b'Vinyl - 10 inch'), (b'vinyl_7', b'Vinyl - 7 inch'), (b'tape', b'Tape')]),
        ),
    ]
