from rest_framework import serializers

from sheets.models import *


class GameTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameTemplate
        fields = '__all__'


class GameSessionSerializer(serializers.ModelSerializer):
    sheets_count = serializers.SerializerMethodField()

    class Meta:
        model = GameSession
        fields = ('id', 'name', 'slug', 'game_template', 'sheets_count')
        depth = 1

    def get_sheets_count(self, instance):
        return CharacterSheet.objects.filter(game_sessions=instance).count()


class CharacterSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterSheet
        fields = '__all__'
        depth = 1
