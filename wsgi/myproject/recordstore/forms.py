from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as DjangoUser
from django.db import models
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget

from datetime import date

from .models import *

class SelectDateCustom(SelectDateWidget):

    def create_select(self, *args, **kwargs):
        select = super(SelectDateCustom, self).create_select(*args, **kwargs)
        return '<div class="col-xs-4">' + select + '</div>'

    def render(self, *args, **kwargs):
        row = super(SelectDateCustom, self).render(*args, **kwargs)
        return '<div class="row">' + row + '</div>'


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

        widgets = {
            'release_date' : SelectDateCustom(years = range(date.today().year, 1900, -1)),
        }

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

class OwnedRecordForm(ModelForm):

    class Meta:
        model = OwnedRecord

        fields = [
            'owner',
            'album',
            'pressing'
        ]

class CreateUserForm(UserCreationForm):

    def save(self):
        django_user = super(CreateUserForm, self).save()
        rs_user = RecordStoreUser(django_user=django_user)
        rs_user.save()
        return rs_user

class EditUserForm(ModelForm):

    class Meta:
        model = DjangoUser

        fields = [
            'first_name',
            'last_name',
        ]

class AlbumReviewForm(ModelForm):
    class Meta:
        model = AlbumReview

        fields = [
            'album',
            'author',
            'text',
        ]

        widgets = {
            'album' : forms.HiddenInput(),
            'author' : forms.HiddenInput(),
        }
