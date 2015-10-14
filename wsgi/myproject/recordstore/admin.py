from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Genre) 

class PressingInline(admin.TabularInline):
    model = Pressing
    extra = 1;

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [PressingInline]

class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1;

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]
