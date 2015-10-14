# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0009_auto_20151014_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressing',
            name='label_address',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='pressing',
            name='label_name',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
