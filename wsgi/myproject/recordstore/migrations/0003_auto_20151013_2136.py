# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0002_auto_20151013_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='date_end',
            field=models.DateTimeField(null=True, verbose_name=b'End Date'),
        ),
    ]
