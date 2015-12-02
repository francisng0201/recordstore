# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0004_albumreview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albumreview',
            options={'ordering': ['date_written']},
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255, unique=True, serialize=False, primary_key=True),
        ),
    ]
