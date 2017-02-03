from django.shortcuts import render
from music_history_api.models import song_model as som
from music_history_api.serializers import song_serializer as sos
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets, renderers, permissions
from django.contrib.auth.models import User


class SongViewSet(viewsets.ModelViewSet):
    """
    The Song View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Order's url for the `update` and `destroy` actions.
    """
    queryset = som.Song.objects.all()
    serializer_class = sos.SongSerializer
