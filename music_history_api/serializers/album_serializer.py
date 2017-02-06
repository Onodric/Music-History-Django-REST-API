from rest_framework import serializers
from music_history_api.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Album

    Author: Ben Marks
    """

    class Meta:
        model = album_model.Album
        fields = '__all__'
        depth = 2

