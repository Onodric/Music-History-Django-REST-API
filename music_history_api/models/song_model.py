from django.db import models
from . import artist_model, genre_model


class Song(models.Model):
    """
    Class to create a table representing a song, to be tied to an artist or group of artists
    Extension of models.Model

    Variables:
        title: the song title
        release_date: the date of release
        author: the song's writer

    Author: Ben Marks
    """
    title = models.CharField(max_length=100, blank=True, default='')
    release_date = models.DateField(auto_now_add=False)
    author = models.CharField(max_length=100, blank=True, default='')
    duration = models.PositiveIntegerField()
    artist = models.ManyToManyField(artist_model.Artist)
    genre = models.ForeignKey(genre_model.Genre, related_name="genre")

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API

        Returns a string representaion of the payment method's name field
        """
        return self.title

    class Meta:
        ordering = ('title',)
