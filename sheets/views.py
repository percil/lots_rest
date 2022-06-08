import django_filters
from django.shortcuts import render
from rest_framework import generics

from sheets.filters import *
from sheets.serializers import *


def default_redirect(request):
    return render(request, 'redirect.html', {})


class GameTemplateListView(generics.ListAPIView):
    queryset = GameTemplate.objects.all()
    serializer_class = GameTemplateSerializer


class GameSessionListView(generics.ListAPIView):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = GameSessionFilter


class GameSessionDetailsView(generics.RetrieveAPIView):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer
    lookup_field = 'id'


class CharacterSheetListView(generics.ListAPIView):
    queryset = CharacterSheet.objects.all()
    serializer_class = CharacterSheetSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = CharacterSheetFilter


class CharacterSheetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CharacterSheet.objects.all()
    serializer_class = CharacterSheetSerializer
    lookup_field = 'slug'
