# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0002_remove_recordstoreuser_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordstoreuser',
            name='friends',
            field=models.ForeignKey(blank=True, to='recordstore.RecordStoreUser', null=True),
        ),
    ]
