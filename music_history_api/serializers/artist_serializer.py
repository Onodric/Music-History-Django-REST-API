from rest_framework import serializers
from music_history_api.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Artist

    Author: Ben Marks
    """

    class Meta:
        model = artist_model.Artist
        fields = '__all__'
