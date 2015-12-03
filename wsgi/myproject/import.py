#!/usr/bin/env python
"""
imports data from the musicbrainz database as a seed for our own
"""
# default python imports
import os
from datetime import datetime 
import pytz
import calendar
import time

# musicbrainz setup
import musicbrainzngs as mb
mb.set_useragent('crawler', '0.0.1')

# Django imports
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
import django
django.setup()
print 'setup django'

import recordstore.models as models

def convert_time(str_time):
    try: 
        time_struct = time.strptime(str_time, '%Y-%m-%d')
        cal_time = calendar.timegm(time_struct)
        dt = datetime.fromtimestamp(cal_time, tz=pytz.utc)
        return dt.date()
    except:
        return None

def import_releases(artist, mb_id):
    releases = mb.browse_releases(artist=mb_id, release_type='album')
    for release in releases['release-list']:
        title = release['title']
        try:
            date = convert_time(release['date'])
        except:
            date = None
        try:
            mb_id = release['id']
        except:
            mb_id = '0'

        result = models.Album.objects.filter(musicbrainz_id=mb_id)
        if len(result) > 0:
            return

        album = models.Album(artist=artist, name=title,
                musicbrainz_id=mb_id)
        album.save()

def import_artist(artist):
    name = artist['name']
    try:
        country = artist['country']
    except:
        country = ''
    mb_id = artist['id']

    result = models.Artist.objects.filter(musicbrainz_id=mb_id)
    if len(result) > 0:
        print u'Skipped {} : {}'.format(name, mb_id).encode('ascii', 'ignore')
        return

    django_artist = models.Artist(country=country, name=name,
            musicbrainz_id=mb_id)
    print u'{} : {}'.format(name, mb_id).encode('ascii', 'ignore')
    django_artist.save()
    import_releases(django_artist, mb_id)

def bulk_import_artist():
    terms = [
        # 'bb king',
        # 'elvis',
        # 'black sabbath',
        # 'fugazi',
        # 'minor threat',
        # 'converge',
        # '\'68',
        # 'old man gloom',
        # 'citizen',
        # 'blues brothers',
        # 'cult of luna',
        # 'our lady',
        # 'so long forgotten',
        # 'cash',
        # 'z',
        # 'ramones',
        # 'kesha',
        # 'nine inch nails',
        # 'bill nye',
        # 'my bloody valentine',
        # 'ride',
        # 'slabdragger',
        # 'slowdive',
        #  'oasis',
        # 'reo',
        # 'cloakroom',
        # 'underoath',
        # 'brand new',
        # 'taking back sunday',
        # 'the cure',
        # 'jesu',
        # 'jesus and the mary chain',
        # 'zozobra',
        # 'cave in',
        # 'led zeppelin',
        'pity sex',
        'looming', 
        'our lady',
    ]
    for search in terms:
        print 'searching {}'.format(search)
        result = mb.search_artists(artist=search, type="group", country="US")
        for artist in result['artist-list']:
            import_artist(artist)

def bulk_import_labels():
    albums = models.Album.objects.all()
    for album in albums:
        title = album.name
        mb_id = album.musicbrainz_id
        print u'{} : {}'.format(title, mb_id).encode('ascii', 'ignore')
        result = mb.browse_labels(release=mb_id)
        try:
            label = result['label-list'][0]  
            name = label['name']
            address = label['country']
            mb_id = label['id']

            if len(models.RecordLabel.objects.filter(musicbrainz_id=mb_id)) == 0:
                label = models.RecordLabel(label_name=name, label_address=address, musicbrainz_id=mb_id)
                label.save()

            pressing = models.Pressing(album=album, label=label)
            pressing.save()
        except:
            continue

if __name__ == "__main__":
    bulk_import_artist()
    print 'done'
