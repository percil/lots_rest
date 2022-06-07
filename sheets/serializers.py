from rest_framework import serializers

from sheets.models import *


class GameTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameTemplate
        fields = '__all__'


class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSession
        fields = '__all__'
        depth = 1


class CharacterSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSheet
        fields = '__all__'
        depth = 1

