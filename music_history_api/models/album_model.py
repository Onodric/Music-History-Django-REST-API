from django.db import models
from . import song_model


class Album(models.Model):
    """
    Class to create a table representing an Album, to be tied to an artist or group of artists and the songs therein.
    Extension of models.Model

    Variables:
        title: the song title
        release_date: the date of release
        author: the song's writer

    Author: Ben Marks
    """
    title = models.CharField(max_length=100, blank=True, default='')
    disc_number = models.PositiveIntegerField()
    disc_total = models.PositiveIntegerField()
    release_date = models.DateField(auto_now_add=False)
    songs = models.ManyToManyField(song_model.Song)
    label = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API

        Returns a string representaion of the payment method's name field
        """
        return self.title

    class Meta:
        ordering = ('title',)
