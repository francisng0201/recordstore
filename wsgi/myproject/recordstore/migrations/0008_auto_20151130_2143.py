# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0007_remove_recordstoreuser_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordstoreuser',
            name='django_user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
