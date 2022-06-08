from django.shortcuts import render
from rest_framework import generics

from sheets.serializers import *


def default_redirect(request):
    return render(request, 'redirect.html', {})


class GameTemplateListView(generics.ListAPIView):
    queryset = GameTemplate.objects.all()
    serializer_class = GameTemplateSerializer


class GameSessionListView(generics.ListAPIView):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer


class CharacterSheetListView(generics.ListAPIView):
    queryset = CharacterSheet.objects.all()
    serializer_class = CharacterSheetSerializer


class CharacterSheetView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CharacterSheet.objects.all()
    serializer_class = CharacterSheetSerializer
    lookup_field = 'slug'
