from rest_framework import serializers
from music_history_api.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Genre

    Author: Ben Marks
    """

    class Meta:
        model = User
        fields = (
            'url',
            'first_name',
            'last_name',
            'username',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'last_login',
            )        


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


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Album

    Author: Ben Marks
    """

    class Meta:
        model = Album
        fields = '__all__'
