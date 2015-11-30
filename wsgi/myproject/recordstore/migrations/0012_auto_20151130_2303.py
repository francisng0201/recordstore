# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0011_auto_20151130_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='rating',
            field=models.IntegerField(default=0, choices=[(-1, b'None'), (0, b'0 Stars'), (1, b'1 Star'), (2, b'2 Stars'), (3, b'3 Stars'), (4, b'4 Stars'), (5, b'5 Stars')]),
        ),
    ]
