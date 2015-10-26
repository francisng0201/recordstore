# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordstore', '0002_auto_20151023_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnedRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='owned_records',
        ),
        migrations.AlterField(
            model_name='album',
            name='rating',
            field=models.IntegerField(default=0, choices=[(0, b'0 Stars'), (1, b'1 Star'), (2, b'2 Stars'), (3, b'3 Stars'), (4, b'4 Stars'), (5, b'5 Stars')]),
        ),
        migrations.AddField(
            model_name='ownedrecord',
            name='album',
            field=models.ForeignKey(to='recordstore.Album'),
        ),
        migrations.AddField(
            model_name='ownedrecord',
            name='owner',
            field=models.ForeignKey(to='recordstore.User'),
        ),
        migrations.AddField(
            model_name='ownedrecord',
            name='pressing',
            field=models.ForeignKey(blank=True, to='recordstore.Pressing', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='ownedrecord',
            unique_together=set([('album', 'pressing')]),
        ),
    ]
