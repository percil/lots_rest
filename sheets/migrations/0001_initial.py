# Generated by Django 4.0.5 on 2022-06-07 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Game Template',
                'verbose_name_plural': 'Game Templates',
            },
        ),
        migrations.CreateModel(
            name='GameSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('game_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheets.gametemplate', verbose_name='Game Template')),
            ],
            options={
                'verbose_name': 'Game Session',
                'verbose_name_plural': 'Game Sessions',
            },
        ),
        migrations.CreateModel(
            name='CharacterSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='Name')),
                ('slug', models.SlugField(default='djangodbmodelsfieldscharfield', max_length=150, null=True, verbose_name='Slug')),
                ('content', models.JSONField(blank=True, null=True)),
                ('game_sessions', models.ManyToManyField(blank=True, to='sheets.gamesession')),
                ('game_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheets.gametemplate', verbose_name='Game Template')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Player')),
            ],
            options={
                'verbose_name': 'Character Sheet',
                'verbose_name_plural': 'Character Sheets',
            },
        ),
    ]
