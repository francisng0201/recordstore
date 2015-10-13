# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0003_auto_20151013_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='country',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
