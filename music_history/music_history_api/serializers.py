from rest_framework import serializers
from .models import *
from django.contrib.auth import models
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Genre

    Author: Ben Marks
    """

    class Meta:
        model = User
        fields = '__all__'        


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Genre

    Author: Ben Marks
    """

    class Meta:
        model = Genre
        fields = '__all__'


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Artist

    Author: Ben Marks
    """

    class Meta:
        model = Artist
        fields = '__all__'


class SongSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Song

    Author: Ben Marks
    """

    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializeer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Album

    Author: Ben Marks
    """

    class Meta:
        model = Album
        fields = '__all__'
