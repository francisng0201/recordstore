from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __unicode__(self):
        return self.name

class Artist(models.Model):
    country = models.CharField(max_length=255, default='')
    date_start = models.DateTimeField('Start Date')
    date_end = models.DateTimeField('End Date', null=True)
    name = models.CharField(max_length=255)
    musicbrainz_id = models.IntegerField(default=0, null=True)

    def __unicode__(self):
        return self.name

    def is_active(self):
        return self.date_end == models.NullField
    
class Album(models.Model):
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre)

    name = models.CharField(max_length=255)
    num_songs = models.IntegerField(default=0)
    release_date = models.DateField('Release Date')

    RATING_CHOICES = (
        (0, '0 Stars'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (4, '5 Stars'),
    )
    rating = models.IntegerField(default=0, choices=RATING_CHOICES)

    def __unicode__(self):
        return self.name 

class Pressing(models.Model):
    album = models.ForeignKey(Album)

    label_name = models.CharField(max_length=255)
    label_address = models.CharField(max_length=255)
    artwork = models.ImageField()

    ALLOWED_FORMATS = (
        ('cd', 'CD'),
        ('vinyl_12', 'Vinyl 12 inch'),
        ('vinyl_7', 'Vinyl 7 inch'),
        ('tape', 'Tape'),
    )
    release_format = models.CharField(max_length=255, choices=ALLOWED_FORMATS, default='')
