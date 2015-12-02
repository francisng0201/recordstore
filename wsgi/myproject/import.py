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
    django_artist = models.Artist(country=country, name=name,
            musicbrainz_id=mb_id)
    print u'{} : {}'.format(name, mb_id).encode('ascii', 'ignore')
    django_artist.save()
    import_releases(django_artist, mb_id)

if __name__ == "__main__":
    result = mb.search_artists(artist="Converge", type="group",
            country="US")
    for artist in result['artist-list']:
        import_artist(artist)
