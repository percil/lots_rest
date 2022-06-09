import json
import urllib.request

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class GameTemplate(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False, verbose_name='Name')
    code = models.SlugField(max_length=150, null=True, blank=False, verbose_name='Slug')
    generator_url = models.URLField(null=True, blank=True, verbose_name='Generator URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game Template'
        verbose_name_plural = 'Game Templates'


class GameSession(models.Model):
    game_template = models.ForeignKey(GameTemplate, on_delete=models.CASCADE, verbose_name='Game Template')
    name = models.CharField(max_length=150, null=False, verbose_name='Name')
    slug = models.SlugField(max_length=150, null=True, blank=False, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game Session'
        verbose_name_plural = 'Game Sessions'


def generate_content(generator_url: str) -> dict:
    endpoint = urllib.request.urlopen(generator_url)
    if endpoint.getcode() == 200:
        data = endpoint.read()
        return json.loads(data)
    return {}


class CharacterSheet(models.Model):
    game_template = models.ForeignKey(GameTemplate, on_delete=models.CASCADE, null=False, verbose_name='Game Template')
    game_sessions = models.ManyToManyField(
        GameSession,
        blank=True
    )

    player = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Player')
    name = models.CharField(max_length=150, null=True, blank=False, verbose_name='Name')
    slug = models.SlugField(max_length=150, null=True, blank=False, verbose_name='Slug')
    content = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if (self.content is None or self.content == {}) and self.game_template.generator_url is not None:
            self.content = generate_content(self.game_template.generator_url)
            if 'name' in self.content:
                self.name = self.content['name']
                self.slug = slugify(self.name)

        super(CharacterSheet, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Character Sheet'
        verbose_name_plural = 'Character Sheets'
