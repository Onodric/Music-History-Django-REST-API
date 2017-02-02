from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets, renderers, permissions
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    The User View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific User's url for the `update` and `destroy` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    """
    The Artist View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Order's url for the `update` and `destroy` actions.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    The Album View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Order's url for the `update` and `destroy` actions.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    """
    The Song View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Order's url for the `update` and `destroy` actions.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class GenreViewSet(viewsets.ModelViewSet):
    """
    The Genre View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Order's url for the `update` and `destroy` actions.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
