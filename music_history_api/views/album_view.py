from django.shortcuts import render
from music_history_api.models import album_model as alm
from music_history_api.serializers import album_serializer as als
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets, renderers, permissions
from django.contrib.auth.models import User


class AlbumViewSet(viewsets.ModelViewSet):
    """
    The Album View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Order's url for the `update` and `destroy` actions.
    """
    queryset = alm.Album.objects.all()
    serializer_class = als.AlbumSerializer
