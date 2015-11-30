# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0003_recordstoreuser_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordstoreuser',
            name='django_user',
        ),
        migrations.RemoveField(
            model_name='recordstoreuser',
            name='profile_picture',
        ),
    ]
