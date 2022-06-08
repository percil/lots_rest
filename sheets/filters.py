from django_filters.rest_framework import FilterSet

from sheets.models import GameSession, CharacterSheet


class GameSessionFilter(FilterSet):
    class Meta:
        model = GameSession
        fields = {
            'game_template': ('exact',)
        }


class CharacterSheetFilter(FilterSet):
    class Meta:
        model = CharacterSheet
        fields = {
            'game_template': ('exact',),
            'game_sessions': ('exact',),
        }
