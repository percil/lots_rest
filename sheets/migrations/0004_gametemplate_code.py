# Generated by Django 4.0.5 on 2022-06-08 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0003_alter_charactersheet_slug_alter_gamesession_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='gametemplate',
            name='code',
            field=models.SlugField(max_length=150, null=True, verbose_name='Slug'),
        ),
    ]