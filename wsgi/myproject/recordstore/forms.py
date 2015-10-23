from django.db import models
from django.forms import ModelForm


from .models import *

class ArtistForm(ModelForm):
    
    class Meta:
        model = Artist

        fields = [
            'name',
            'country',
            'musicbrainz_id',
            'date_start',
            'date_end',
        ]

class GenreForm(ModelForm):
    
    class Meta:
        model = Genre

        fields = [
            'name',
        ]

class AlbumForm(ModelForm):
    
    class Meta:
        model = Album

        fields = [
            'artist',
            'genre',
            'name',
            'num_songs',
            'release_date',
            'rating',
        ]

class PressingForm(ModelForm):

    class Meta:
        model = Pressing

        fields = [
            'album',
            'label',
            'artwork',
            'version_number',
            'release_format',
        ]

class RecordLabelForm(ModelForm):

    class Meta:
        model = RecordLabel

        fields = [
            'label_name',
            'label_address',
        ]
