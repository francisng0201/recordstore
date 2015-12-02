# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0003_recordlabel_musicbrainz_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=500)),
                ('date_written', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(to='recordstore.Album')),
                ('author', models.ForeignKey(to='recordstore.RecordStoreUser')),
            ],
        ),
    ]
