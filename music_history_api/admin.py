from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(artist_model.Artist)
admin.site.register(album_model.Album)
admin.site.register(genre_model.Genre)
admin.site.register(song_model.Song)