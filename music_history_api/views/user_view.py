from django.shortcuts import render
from music_history_api.models import *
from music_history_api.serializers import user_serializer as uss
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
    serializer_class = uss.UserSerializer
