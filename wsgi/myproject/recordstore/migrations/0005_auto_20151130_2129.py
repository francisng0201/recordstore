# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recordstore', '0004_auto_20151130_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordstoreuser',
            name='django_user',
            field=models.OneToOneField(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recordstoreuser',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
