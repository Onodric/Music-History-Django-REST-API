from django.db import models


class Genre(models.Model):
    """
    Class to create a table representing a Genre, to be tied to an song.
    Extension of models.Model

    Variables:
        title: the song title

    Author: Ben Marks
    """
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API

        Returns a string representaion of the payment method's name field
        """
        return self.name

    class Meta:
        ordering = ('name',)
