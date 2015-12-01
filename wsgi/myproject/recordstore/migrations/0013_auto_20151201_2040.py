# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0012_auto_20151130_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordlabel',
            name='label_name',
            field=models.CharField(unique=True, max_length=255, blank=True),
        ),
    ]
