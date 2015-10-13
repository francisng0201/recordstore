from django.db import models
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

class Artist(models.Model):
    country = models.CharField(max_length=255, default='')
    date_start = models.DateTimeField('Start Date')
    date_end = models.DateTimeField('End Date', null=True)
    name = models.CharField(max_length=255)
    musicbrainz_id = models.IntegerField(default=0, null=True)
    
class Album(models.Model):
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre)

    name = models.CharField(max_length=255)
    num_songs = models.IntegerField(default=0)
    release_date = models.DateField('Release Date')

    ALLOWED_FORMATS = (
        ('cd', 'CD'),
        ('vinyl_12', 'Vinyl 12 inch'),
        ('vinyl_7', 'Vinyl 7 inch'),
        ('tape', 'Tape'),
    )
    release_format = models.CharField(max_length=255, choices=ALLOWED_FORMATS)

class Pressing(models.Model):
    album = models.ForeignKey(Album)

    label_name = models.CharField(max_length=255)
    label_address = models.CharField(max_length=255)
    artwork = models.ImageField()

