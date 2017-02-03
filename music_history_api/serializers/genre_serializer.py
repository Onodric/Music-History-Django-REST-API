from rest_framework import serializers
from music_history_api.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Genre

    Author: Ben Marks
    """

    class Meta:
        model = genre_model.Genre
        fields = '__all__'
