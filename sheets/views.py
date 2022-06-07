from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

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
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = CharacterSheet.objects.all()
    serializer_class = CharacterSheetSerializer


class CharacterSheetView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = CharacterSheet.objects.all()
    serializer_class = CharacterSheetSerializer
    lookup_field = 'slug'
