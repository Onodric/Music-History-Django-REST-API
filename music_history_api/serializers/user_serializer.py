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

