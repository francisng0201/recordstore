# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0010_auto_20151130_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pressing',
            name='label',
            field=models.ForeignKey(blank=True, to='recordstore.RecordLabel', null=True),
        ),
    ]
