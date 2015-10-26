from django.contrib.auth.models import User as ModelUser
from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __unicode__(self):
        return self.name

class RecordLabel(models.Model):
    label_name = models.CharField(max_length=255, blank=True)
    label_address = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.label_name

class Artist(models.Model):
    country = models.CharField(max_length=255, default='', blank=True)
    date_start = models.DateField('Start Date', blank=True, null=True)
    date_end = models.DateField('End Date', null=True, blank=True)
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
    release_date = models.DateField('Release Date', blank=True, null=True)

    RATING_CHOICES = (
        (0, '0 Stars'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    rating = models.IntegerField(default=0, choices=RATING_CHOICES)

    def __unicode__(self):
        return self.name 

    def is_good(self):
        return self.rating >= 3

class Pressing(models.Model):
    album = models.ForeignKey(Album)
    label = models.ForeignKey(RecordLabel)

    artwork = models.ImageField(null=True, blank=True)
    version_number = models.IntegerField(default=1)

    ALLOWED_FORMATS = (
        ('', 'Unknown'),
        ('cd', 'CD'),
        ('vinyl_12', 'Vinyl - 12 inch'),
        ('vinyl_10', 'Vinyl - 10 inch'),
        ('vinyl_7', 'Vinyl - 7 inch'),
        ('tape', 'Tape'),
    )
    release_format = models.CharField(max_length=255, choices=ALLOWED_FORMATS, default='')

    def __unicode__(self):
        return "{} : {}".format(self.album, self.get_release_format_display())

class User(models.Model):
    user = models.OneToOneField(ModelUser)

    profile_picture = models.ImageField(null=True, blank=True)

    friends = models.ManyToManyField('self', blank=True)

    def __unicode__(self):
        return '{}'.format(self.user)

class OwnedRecord(models.Model):
    owner = models.ForeignKey(User)
    
    album = models.ForeignKey(Album)
    pressing = models.ForeignKey(Pressing, blank=True, null=True)

    class Meta:
        unique_together = ('album', 'pressing',)

    def __unicode__(self):
        if self.pressing == None:
            return '{}'.format(self.album)
        else:
            return '{}'.format(self.pressing)

    def save(self, *args, **kwargs):
        if self.pressing == None:
            super(OwnedRecord, self).save(*args, **kwargs)

