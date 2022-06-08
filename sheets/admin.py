from django.contrib import admin

from sheets.models import GameTemplate, GameSession, CharacterSheet


@admin.register(GameTemplate)
class AdminGameTemplate(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(GameSession)
class AdminGameSession(admin.ModelAdmin):
    list_display = ('name', 'game_template')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CharacterSheet)
class AdminCharacterSheet(admin.ModelAdmin):
    list_display = ('name', 'game_template')
    prepopulated_fields = {'slug': ('name',)}
