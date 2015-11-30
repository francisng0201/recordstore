# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0008_auto_20151130_2143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='pressing',
            options={'ordering': ['album', 'release_format']},
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(blank=True, to='recordstore.Genre', null=True),
        ),
    ]
