# Generated by Django 4.0.5 on 2022-06-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0004_gametemplate_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='gametemplate',
            name='generator_url',
            field=models.URLField(blank=True, null=True, verbose_name='Generator URL'),
        ),
    ]
