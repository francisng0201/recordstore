# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0008_auto_20151014_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(null=True, verbose_name=b'Release Date', blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='date_end',
            field=models.DateField(null=True, verbose_name=b'End Date', blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='date_start',
            field=models.DateField(null=True, verbose_name=b'Start Date', blank=True),
        ),
        migrations.AlterField(
            model_name='pressing',
            name='artwork',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
