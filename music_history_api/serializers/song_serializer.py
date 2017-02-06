from rest_framework import serializers
from music_history_api.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User


class SongSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Song

    Author: Ben Marks
    """

    class Meta:
        model = song_model.Song
        fields = '__all__'
        depth = 1
