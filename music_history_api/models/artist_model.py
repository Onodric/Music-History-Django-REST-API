from django.db import models


class Artist(models.Model):
    """
    Class to create a table representing an artist
    Extension of models.Model

    Variables:
        name: the artist title
        date_formed: the date of release

    Author: Ben Marks
    """
    name = models.CharField(max_length=100, blank=True, default='')
    date_formed = models.DateField(auto_now_add=False)

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API

        Returns a string representaion of the payment method's name field
        """
        return self.name

    class Meta:
        ordering = ('name',)
