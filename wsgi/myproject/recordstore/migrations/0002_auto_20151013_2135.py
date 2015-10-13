# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='musicbrainz_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
