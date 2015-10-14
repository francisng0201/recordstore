# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0006_auto_20151014_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='country',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='date_end',
            field=models.DateTimeField(null=True, verbose_name=b'End Date', blank=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='date_start',
            field=models.DateTimeField(null=True, verbose_name=b'Start Date', blank=True),
        ),
    ]
