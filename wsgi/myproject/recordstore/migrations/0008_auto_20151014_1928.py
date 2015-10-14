# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0007_auto_20151014_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressing',
            name='version_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='pressing',
            name='artwork',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='pressing',
            name='label_address',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AlterField(
            model_name='pressing',
            name='label_name',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
