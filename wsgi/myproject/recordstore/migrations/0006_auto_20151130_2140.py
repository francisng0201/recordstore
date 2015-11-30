# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0005_auto_20151130_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordstoreuser',
            name='friends',
            field=models.ForeignKey(default=None, to='recordstore.RecordStoreUser'),
            preserve_default=False,
        ),
    ]
