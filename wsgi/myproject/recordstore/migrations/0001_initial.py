# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('num_songs', models.IntegerField(default=0)),
                ('release_date', models.DateField(verbose_name=b'Release Date')),
                ('release_format', models.CharField(max_length=255, choices=[(b'cd', b'CD'), (b'vinyl_12', b'Vinyl 12 inch'), (b'vinyl_7', b'Vinyl 7 inch'), (b'tape', b'Tape')])),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=255)),
                ('date_start', models.DateTimeField(verbose_name=b'Start Date')),
                ('date_end', models.DateTimeField(verbose_name=b'End Date')),
                ('name', models.CharField(max_length=255)),
                ('musicbrainz_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('name', models.CharField(max_length=255, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pressing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label_name', models.CharField(max_length=255)),
                ('label_address', models.CharField(max_length=255)),
                ('artwork', models.ImageField(upload_to=b'')),
                ('album', models.ForeignKey(to='recordstore.Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='recordstore.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(to='recordstore.Genre'),
        ),
    ]
