from django.contrib.auth.models import User as ModelUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db import models
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=255, primary_key=True, unique=True)

    def __unicode__(self):
        return self.name

class RecordLabel(models.Model):
    label_name = models.CharField(max_length=255, blank=True, unique=True)
    label_address = models.CharField(max_length=255, blank=True)
    musicbrainz_id = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.label_name

class Artist(models.Model):
    country = models.CharField(max_length=255, default='', blank=True)
    date_start = models.DateField('Start Date', blank=True, null=True)
    date_end = models.DateField('End Date', null=True, blank=True)
    name = models.CharField(max_length=255)
    musicbrainz_id = models.CharField(default='', null=True,
            max_length=255)

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name

    def is_active(self):
        return self.date_end == models.NullField
    
class Album(models.Model):
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre, null=True, blank=True)

    name = models.CharField(max_length=255)
    num_songs = models.IntegerField(default=0)
    release_date = models.DateField('Release Date', blank=True, null=True)

    RATING_CHOICES = (
        (-1, 'None'),
        (0, '0 Stars'),
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    rating = models.IntegerField(default=3, choices=RATING_CHOICES)
    musicbrainz_id = models.CharField(default='', null=True,
            max_length=255)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name 

    def is_good(self):
        return self.rating >= 3

class Pressing(models.Model):
    album = models.ForeignKey(Album)
    label = models.ForeignKey(RecordLabel, null=True, blank=True)

    artwork = models.ImageField(null=True, blank=True)
    version_number = models.IntegerField(default=1)

    ALLOWED_FORMATS = (
        ('', 'Unknown Format'),
        ('cd', 'CD'),
        ('vinyl_12', 'Vinyl - 12 inch'),
        ('vinyl_2_12', 'Vinyl - Double LP 12 inch'),
        ('vinyl_10', 'Vinyl - 10 inch'),
        ('vinyl_7', 'Vinyl - 7 inch'),
        ('tape', 'Tape'),
    )
    release_format = models.CharField(max_length=255, choices=ALLOWED_FORMATS, default='')

    class Meta:
        ordering = ['album', 'release_format',]

    def __unicode__(self):
        return "{} : {} : {}".format(self.album.artist, self.album, self.get_release_format_display())

class RecordStoreUser(models.Model):
    django_user = models.OneToOneField(ModelUser, null=True)
    profile_picture = models.ImageField(null=True, blank=True)
    # friends = models.ForeignKey('self')

    def __unicode__(self):
        return '{}'.format(self.django_user)

class OwnedRecord(models.Model):
    owner = models.ForeignKey(RecordStoreUser)
    
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
        else:
            # make sure the album is actually associated with the pressing
            if self.pressing in self.album.pressing_set.all():
                super(OwnedRecord, self).save(*args, **kwargs)
            else:
                raise ValidationError('Pressing must be in this album\'s pressing set')

class AlbumReview(models.Model):
    album = models.ForeignKey(Album)
    author = models.ForeignKey(RecordStoreUser)
    text = models.CharField(max_length=500)

    date_written = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_written',]

    def __unicode__(self):
        return self.text
