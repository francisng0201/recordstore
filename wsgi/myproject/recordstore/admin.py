from django.contrib import admin
from django import forms

from .models import *

# Register your models here.

admin.site.register(Genre) 
admin.site.register(RecordLabel)

class PressingInline(admin.StackedInline):
    model = Pressing
    extra = 1

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [PressingInline]

class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]

class OwnedRecordInline(admin.StackedInline):
    model = OwnedRecord
    extra = 1

@admin.register(RecordStoreUser)
class UserAdmin(admin.ModelAdmin):
    inlines = [OwnedRecordInline,]
