# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('num_songs', models.IntegerField(default=0)),
                ('release_date', models.DateField(null=True, verbose_name=b'Release Date', blank=True)),
                ('rating', models.IntegerField(default=0, choices=[(0, b'0 Stars'), (1, b'1 Star'), (2, b'2 Stars'), (3, b'3 Stars'), (4, b'4 Stars'), (4, b'5 Stars')])),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(default=b'', max_length=255, blank=True)),
                ('date_start', models.DateField(null=True, verbose_name=b'Start Date', blank=True)),
                ('date_end', models.DateField(null=True, verbose_name=b'End Date', blank=True)),
                ('name', models.CharField(max_length=255)),
                ('musicbrainz_id', models.IntegerField(default=0, null=True)),
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
                ('artwork', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('version_number', models.IntegerField(default=1)),
                ('release_format', models.CharField(default=b'', max_length=255, choices=[(b'', b'Unknown'), (b'cd', b'CD'), (b'vinyl_12', b'Vinyl 12 inch'), (b'vinyl_7', b'Vinyl 7 inch'), (b'tape', b'Tape')])),
                ('album', models.ForeignKey(to='recordstore.Album')),
            ],
        ),
        migrations.CreateModel(
            name='RecordLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label_name', models.CharField(max_length=255, blank=True)),
                ('label_address', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', to='recordstore.User', blank=True)),
                ('owned_records', models.ManyToManyField(to='recordstore.Pressing', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pressing',
            name='label',
            field=models.ForeignKey(to='recordstore.RecordLabel'),
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
